import struct
import zlib
from typing import Callable

import google.protobuf.message
from typing.io import BinaryIO

from naobackend.flightlog import VisualizerParameter
from naobackend.proto.log_pb2 import LogEntry
from naobackend.proto.visualizer_pb2 import VisualizerTransaction


class _FlightlogFile:
    def __init__(self):
        pass

    def read(self, size: int) -> bytes:
        pass


class _FlightlogFileRaw(_FlightlogFile):
    __fp: BinaryIO

    def __init__(self, filename: str):
        super().__init__()
        self.__fp = open(filename, "rb")

    def read(self, size: int) -> bytes:
        return self.__fp.read(size)


class _FlightlogFileZlibCompressed(_FlightlogFile):
    __fp: BinaryIO
    __data: bytes

    def __init__(self, filename: str):
        super().__init__()
        self.__fp = open(filename, "rb")
        self.__decompressor = zlib.decompressobj()
        self.__data = bytes()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__fp.close()

    def read(self, length: int) -> bytes:
        if len(self.__data) >= length:
            data = self.__data[:length]
            self.__data = self.__data[length:]
            return data

        while len(self.__data) < length:
            data = self.__fp.read(1024 * 1024)

            if len(data) == 0:
                if len(self.__data) > 0:
                    data = self.__data;
                    self.__data = bytes()
                    return data;
                else:
                    return bytes()

            self.__data += self.__decompressor.decompress(data)

        data = self.__data[:length]
        self.__data = self.__data[length:]
        return data


class FlightlogFile:
    _fp: _FlightlogFile
    _parameter_subscribers: dict[str, list[Callable[[VisualizerParameter], None]]]
    parameter: dict

    def __init__(self, filename: str):
        self.parameter = dict()
        self._parameter_subscribers = dict()
        if filename.endswith(".z"):
            self._fp = _FlightlogFileZlibCompressed(filename)
        else:
            self._fp = _FlightlogFileRaw(filename)

    def subscribe_parameter(self, name: str, callback: Callable[[VisualizerParameter], None]):
        if name not in self._parameter_subscribers:
            self._parameter_subscribers[name] = [callback]
        else:
            self._parameter_subscribers[name].append(callback)

    def filter(self, filter_cb: Callable[[LogEntry], bool]) -> [LogEntry]:
        log_entries = []
        while True:
            log_entry = self.next()
            if log_entry is None:
                break

            if filter_cb(log_entry):
                log_entries.append(log_entry)

        return log_entries

    def next(self) -> LogEntry | None:
        log_entry_length = self._fp.read(4)

        if len(log_entry_length) == 0:
            return None

        length = struct.unpack("<i", log_entry_length)[0]
        log_entry = LogEntry()
        buf = self._fp.read(length)

        if len(buf) == 0:
            return None

        if len(buf) < length:
            print("Error reading the log entry. Reason unknown!")

        log_entry.ParseFromString(buf)

        if log_entry.subsystem == "VisualizerFileLog" and log_entry.typeinfo == "Transaction":
            self._process_visual_transaction(log_entry)

        return log_entry

    def read(self) -> [LogEntry]:
        log_entries = []
        while True:
            log_entry = self.next()
            if log_entry is None:
                break
            log_entries.append(log_entry)

        return log_entries

    def process(self):
        while True:
            log_entry = self.next()
            if log_entry is None:
                break

    def _process_visual_transaction(self, log_entry: LogEntry):
        vis = VisualizerTransaction()

        try:
            vis.ParseFromString(log_entry.logEntry[4:])
        except google.protobuf.message.DecodeError as e:
            return

        updated_parameter = False
        for p in vis.parameter:
            if vis.subsystem not in self.parameter.keys():
                self.parameter[vis.subsystem] = VisualizerParameter(vis.subsystem)

            self.parameter[vis.subsystem].recv_time = vis.time
            if len(p.floatParams) > 0:
                self.parameter[vis.subsystem].entries[p.name] = p.floatParams
            else:
                self.parameter[vis.subsystem].entries[p.name] = p.intParams

            updated_parameter = True

        if updated_parameter and vis.subsystem in self._parameter_subscribers:
            for subscriber in self._parameter_subscribers[vis.subsystem]:
                subscriber(self.parameter[vis.subsystem])
