from __future__ import annotations

import io
import socket
from enum import Enum
from typing import Callable

from naobackend.visualizer_datatype import *


class RobotOptionType(Enum):
    INT = 0
    FLOAT = 1
    BOOL = 2
    ENUM = 3


class RobotOption:
    name: str

    @staticmethod
    def parse(fp: io.BufferedIOBase, option_sender: Callable[[str, bytes], None]):
        """"""


class RobotOptionInt(RobotOption):
    size: int
    min: int
    max: int
    step: int
    _value: int

    def __init__(self, option_sender: Callable[[str, bytes], None], name: str, size: int, min: int, max: int, step: int,
                 value: int):
        self.name = name
        self.size = size
        self.min = min
        self.max = max
        self.step = step
        self._value = value
        self._option_sender = option_sender

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, v: int):
        buf = io.BytesIO()
        match self.size:
            case 1:
                write_byte(buf, v)
            case 2:
                write_short(buf, v)
            case 4:
                write_int(buf, v)
            case _:
                raise ValueError("Unknown integer type to set")

        self._option_sender(self.name, buf.getvalue())
        buf.close()
        self._value = v

    @staticmethod
    def parse(fp: io.BufferedIOBase, option_sender: Callable[[str, bytes], None]):
        name = read_string(fp)
        size = read_byte(fp)

        if size not in (1, 2, 4):
            print("Can't parse int robot option. Unknown type with size: " + str(size))
            return

        match size:
            case 1:
                min = read_byte(fp)
                max = read_byte(fp)
                step = read_byte(fp)
                value = read_byte(fp)
                return RobotOptionInt(option_sender, name, size, min, max, step, value)
            case 2:
                min = read_short(fp)
                max = read_short(fp)
                step = read_short(fp)
                value = read_short(fp)
                return RobotOptionInt(option_sender, name, size, min, max, step, value)
            case 4:
                min = read_int(fp)
                max = read_int(fp)
                step = read_int(fp)
                value = read_int(fp)
                return RobotOptionInt(option_sender, name, size, min, max, step, value)
            case _:
                raise ValueError("Integer type unknown")


class RobotOptionFloat(RobotOption):
    min: float
    max: float
    step: float
    _value: float

    def __init__(self, option_sender: Callable[[str, bytes], None], name: str, min: float, max: float, step: float, value: float):
        self.name = name
        self.min = min
        self.max = max
        self.step = step
        self._value = value
        self._option_sender = option_sender

    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, v: float):
        buf = io.BytesIO()
        write_float(buf, v)
        self._option_sender(self.name, buf.getvalue())
        buf.close()
        self._value = v

    @staticmethod
    def parse(fp: io.BufferedIOBase, option_sender: Callable[[str, bytes], None]):
        name = read_string(fp)
        min = read_float(fp)
        max = read_float(fp)
        step = read_float(fp)
        value = read_float(fp)
        return RobotOptionFloat(option_sender, name, min, max, step, value)


class RobotOptionBool(RobotOption):
    _value: bool

    def __init__(self, option_sender: Callable[[str, bytes], None], name: str, value: bool):
        self.name = name
        self._value = value
        self._option_sender = option_sender

    @property
    def value(self) -> bool:
        return self._value

    @value.setter
    def value(self, v: bool):
        buf = io.BytesIO()
        write_byte(buf, 1 if v is True else 0)
        self._option_sender(self.name, buf.getvalue())
        buf.close()
        self._value = v

    @staticmethod
    def parse(fp: io.BufferedIOBase, option_sender: Callable[[str, bytes], None]):
        name = read_string(fp)
        value = True if read_byte(fp) > 0 else False
        return RobotOptionBool(option_sender, name, value)


class RobotOptionEnum(RobotOption):
    _value: int

    def __init__(self, option_sender: Callable[[str, bytes], None], name: str, value: int, items: dict[str, int]):
        self.name = name
        self._value = value
        self.items = items
        self._option_sender = option_sender

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, v: int):
        buf = io.BytesIO()
        write_int(buf, v)
        self._option_sender(self.name, buf.getvalue())
        buf.close()
        self._value = v

    @staticmethod
    def parse(fp: io.BufferedIOBase, option_sender: Callable[[str, bytes], None]):
        name = read_string(fp)
        value = read_int(fp)
        item_count = read_int(fp)
        items = dict()

        for c in range(item_count):
            item_name = read_string(fp)
            item_id = read_int(fp)
            items[item_name] = item_id

        return RobotOptionFloat(option_sender, name, value, items)


class RobotOptionSet:
    name: str
    options: dict[str, RobotOption]

    def __init__(self, fp: io.BufferedIOBase, option_sender: Callable[[str, str, bytes], None]):
        self.name = read_string(fp)
        self.options = dict()
        option_count = read_int(fp)
        def my_option_sender(option_name: str, option_contents: bytes): option_sender(self.name, option_name, option_contents)

        for i in range(option_count):
            option_type = read_byte(fp)

            match RobotOptionType(option_type):
                case RobotOptionType.INT:
                    opt = RobotOptionInt.parse(fp, my_option_sender)
                case RobotOptionType.FLOAT:
                    opt = RobotOptionFloat.parse(fp, my_option_sender)
                case RobotOptionType.BOOL:
                    opt = RobotOptionBool.parse(fp, my_option_sender)

            self.options[opt.name] = opt


class RobotOptionCollection:
    option_sets: dict[str, RobotOptionSet]

    __socket: socket.socket
    __fp: io.BufferedRWPair

    __MAGIC_BYTES = 0xabfb3c2a
    __VERSION = 1

    def __init__(self):
        """"""
        self.__socket = None
        self.__fp = None
        self.option_sets = dict()

    def connect(self, ip_addr, port):
        self.__socket = socket.create_connection((ip_addr, port))
        self.__fp = self.__socket.makefile("rwb")
        self.__read_available_options()
        return self

    def __read_available_options(self):
        magic_bytes, version, option_type, option_count = struct.unpack("<Ibbi", self.__fp.read(10))

        if magic_bytes != self.__MAGIC_BYTES:
            raise ValueError("In option set the magic bytes does not map! " + str(magic_bytes))

        if version != self.__VERSION:
            raise ValueError("Version of the reply is unknown please investigate!" + str(version))

        if option_type != 0:
            raise ValueError("Type does not indicate a optionset!" + str(option_type))

        for i in range(option_count):
            length = read_int(self.__fp)
            oset = RobotOptionSet(self.__fp, lambda x, y, z: self._send_value(x, y, z))
            self.option_sets[oset.name] = oset

    def _send_value(self, optionset_name: str, option_name: str, buf_option: bytes):
        buf = io.BytesIO()
        write_string(buf, optionset_name)
        write_string(buf, option_name)
        write_int(buf, len(buf_option))
        buf.write(buf_option)

        self.__fp.write(buf.getvalue())
        self.__fp.flush()
        buf.close()


class RobotOptionConnection:
    PORT_FIRMWARE = 9994
    PORT_BRIDGE = 9996

    bridge_options: RobotOptionCollection
    firmware_options: RobotOptionCollection

    def __init__(self):
        """"""
        self.__s_bridge = None
        self.__s_firmware = None

    def connect(self, ip_addr: str, port_firmware: int = PORT_FIRMWARE, port_bridge: int = PORT_BRIDGE):
        self.__s_firmware = socket.create_connection((ip_addr, port_firmware))
        self.__s_bridge = socket.create_connection((ip_addr, port_bridge))

        self.bridge_options = RobotOptionCollection().connect(ip_addr, port_bridge)
        self.firmware_options = RobotOptionCollection().connect(ip_addr, port_firmware)

