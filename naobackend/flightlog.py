import socket
import struct
import threading
from enum import Enum
from queue import SimpleQueue
from typing import Callable, Sequence

import google.protobuf.message

from naobackend.lola_status import LolaStatus
from naobackend.lola_status import convert_from_proto as lola_status_convert_from_proto
from naobackend.proto.log_pb2 import LogEntry
from naobackend.proto.lola_lowlevel_pb2 import LolaStatus as LolaStatusPB
from naobackend.proto.visualizer_pb2 import VisualizerTransaction
from naobackend.proto.worldmodel_pb2 import FirmwareInfo


class VisualizerParameter:
    name: str
    recv_time: int
    entries: dict[str, Sequence[float | int]]

    def flatten(self) -> dict[str, any]:
        d = dict()

        for k, v in self.entries.items():
            d[f"{self.name}.{k}"] = v[0] if len(v) == 1 else v

        return d

    def __init__(self, name: str):
        self.name = name
        self.recv_time = 0
        self.entries = dict()

    def __str__(self):
        return f"VisualParamter: name={self.name} recv_time={self.recv_time} entries={str(self.entries)}"


class LogEntryType(Enum):
    VISUAL_TRANSACTION = 0,
    LOLA_STATUS_INFO = 1
    LOG_ENTRY = 2


class Flightlog:
    elements: SimpleQueue[LogEntry]
    _log_entry_queue: SimpleQueue[(LogEntryType, LogEntry)]
    _parameter_subscribers: dict[str, list[Callable[[VisualizerParameter], None]]]
    _parameter_flat_subscribers: list[Callable[[dict[str, any]], None]]
    _log_entry_subscribers: dict[tuple[str, str], list[Callable[[LogEntry], None]]]
    _lola_debug_frames_subscribers: list[Callable[[LolaStatus], None]]
    _lola_debug_frames_flat_subscribers: list[Callable[[dict[str, float]], None]]
    _parameter_waiter: dict[str, threading.Event]
    parameter: dict[VisualizerParameter]

    max_items_in_queue = 1000

    def __init__(self, ipaddr: str, port: int = 9995):
        self._log_message_subscribers = list()
        self.elements = SimpleQueue()
        self._log_entry_queue = SimpleQueue()
        self.parameter = dict()
        self._parameter_subscribers = dict()
        self._parameter_flat_subscribers = list()
        self._lola_debug_frames_subscribers = list()
        self._lola_debug_frames_flat_subscribers = list()
        self._log_entry_subscribers = {
            ("WMSender", "SendWM"): [self._subscriber_firmware_info],
        }
        self._firmware_info_subscribers = list()
        self._parameter_waiter = dict()
        threading.Thread(target=self._reader, name="FlightLogReader", args=(ipaddr, port), daemon=True).start()
        threading.Thread(target=self._subscriber_updater, name="FlightLogVisualizer", daemon=True).start()

    def wait_for_parameter(self, subsystem: str, timeout=None) -> bool:
        if subsystem in self.parameter:
            return True

        w = threading.Event()
        self._parameter_waiter[subsystem] = w
        return w.wait(timeout)

    def subscribe_parameter(self, name: str, callback: Callable[[VisualizerParameter], None]):
        if name not in self._parameter_subscribers:
            self._parameter_subscribers[name] = [callback]
        else:
            self._parameter_subscribers[name].append(callback)

    def subscribe_parameter_flat(self, callback: Callable[[dict[str, any]], None]):
        self._parameter_flat_subscribers.append(callback)

    def subscribe_lola_debug(self, callback: Callable[[LolaStatus], None]):
        if callable not in self._lola_debug_frames_subscribers:
            self._lola_debug_frames_subscribers.append(callback)

    def subscribe_lola_debug_flat(self, callback: Callable[[dict[str, float]], None]):
        if callable not in self._lola_debug_frames_flat_subscribers:
            self._lola_debug_frames_flat_subscribers.append(callback)

    def subscribe_log_entry(self, subsystem: str, typeinfo: str, callback: Callable[[LogEntry], None]):
        if (subsystem, typeinfo) not in self._log_entry_subscribers:
            self._log_entry_subscribers[(subsystem, typeinfo)] = [callback]
        else:
            self._log_entry_subscribers[(subsystem, typeinfo)].append(callback)

    def _subscriber_updates_visualizer_processor(self, entry: LogEntry):
        vis = VisualizerTransaction()

        try:
            vis.ParseFromString(entry.logEntry[4:])
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

        if vis.subsystem in self._parameter_waiter:
            self._parameter_waiter[vis.subsystem].set()
            self._parameter_waiter.pop(vis.subsystem)

        if updated_parameter and vis.subsystem in self._parameter_subscribers:
            for subscriber in self._parameter_subscribers[vis.subsystem]:
                subscriber(self.parameter[vis.subsystem])

        if updated_parameter and len(self._parameter_flat_subscribers) > 0:
            for subscriber in self._parameter_flat_subscribers:
                subscriber(self.parameter[vis.subsystem].flatten())

    def _subscriber_updates_lola_connector(self, entry: LogEntry):

        if len(self._lola_debug_frames_subscribers) == 0 and len(self._lola_debug_frames_flat_subscribers) == 0:
            return

        lola_status_pb = LolaStatusPB()

        try:
            lola_status_pb.ParseFromString(entry.logEntry)
        except google.protobuf.message.DecodeError as e:
            return

        lola_status = lola_status_convert_from_proto(lola_status_pb)

        for subscriber in self._lola_debug_frames_subscribers:
            subscriber(lola_status)

        if len(self._lola_debug_frames_flat_subscribers) > 0:
            lola_status_dict = lola_status.flatten()
            for subscriber in self._lola_debug_frames_flat_subscribers:
                subscriber(lola_status_dict)

    def _subscriber_updates_log_entries(self, entry: LogEntry):

        if len(self._log_entry_subscribers) == 0:
            return

        subscribers = self._log_entry_subscribers.get((entry.subsystem, entry.typeinfo), [])
        if len(subscribers) == 0:
            return

        for subscriber in subscribers:
            subscriber(entry)

    def subscribe_firmware_info(self, callback: Callable[[FirmwareInfo], None]):
        self._firmware_info_subscribers.append(callback)

    def _subscriber_firmware_info(self, entry: LogEntry):
        firmware_info = FirmwareInfo()
        firmware_info.ParseFromString(entry.logEntry)

        for subscriber in self._firmware_info_subscribers:
            subscriber(firmware_info)


    def _subscriber_updater(self):
        while True:
            entry = self._log_entry_queue.get()

            if entry[0] == LogEntryType.VISUAL_TRANSACTION:
                self._subscriber_updates_visualizer_processor(entry[1])
                continue
            if entry[0] == LogEntryType.LOLA_STATUS_INFO:
                self._subscriber_updates_lola_connector(entry[1])
                continue
            if entry[0] == LogEntryType.LOG_ENTRY:
                self._subscriber_updates_log_entries(entry[1])
                continue

    def _reader(self, ipaddr: str, port: int):
        sock = socket.create_connection((ipaddr, port))
        fp = sock.makefile("rb")

        while True:
            length = struct.unpack("<i", fp.read(4))[0]
            log_entry = LogEntry()
            buf = fp.read(length)

            if len(buf) < length:
                print("Error reading the log entry. Reason unknown!")

            log_entry.ParseFromString(buf)
            self.elements.put(log_entry)

            if log_entry.subsystem == "VisualizerFileLog" and log_entry.typeinfo == "Transaction":
                self._log_entry_queue.put((LogEntryType.VISUAL_TRANSACTION, log_entry))
            elif log_entry.subsystem == "LolaConnector" and log_entry.typeinfo == "LolaDebugFrame":
                self._log_entry_queue.put((LogEntryType.LOLA_STATUS_INFO, log_entry))
            else:
                self._log_entry_queue.put((LogEntryType.LOG_ENTRY, log_entry))

            # print(f"{log_entry.subsystem} {log_entry.typeinfo}")

            while self.elements.qsize() > self.max_items_in_queue:
                self.elements.get()
