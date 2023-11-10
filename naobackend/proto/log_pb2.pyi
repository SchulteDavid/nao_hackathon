from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

BINARY: LogType
BRIDGE: LogSource
DEBUG: LogLevel
DESCRIPTOR: _descriptor.FileDescriptor
ERROR: LogLevel
FIRMWARE: LogSource
INFO: LogLevel
PROTOBUF: LogType
TEXT: LogType
WARN: LogLevel

class LogEntry(_message.Message):
    __slots__ = ["logEntry", "logLevel", "logType", "size", "src", "subsystem", "timestamp", "typeinfo"]
    LOGENTRY_FIELD_NUMBER: _ClassVar[int]
    LOGLEVEL_FIELD_NUMBER: _ClassVar[int]
    LOGTYPE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SRC_FIELD_NUMBER: _ClassVar[int]
    SUBSYSTEM_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    TYPEINFO_FIELD_NUMBER: _ClassVar[int]
    logEntry: bytes
    logLevel: LogLevel
    logType: LogType
    size: int
    src: LogSource
    subsystem: str
    timestamp: int
    typeinfo: str
    def __init__(self, timestamp: _Optional[int] = ..., logLevel: _Optional[_Union[LogLevel, str]] = ..., logType: _Optional[_Union[LogType, str]] = ..., subsystem: _Optional[str] = ..., size: _Optional[int] = ..., logEntry: _Optional[bytes] = ..., typeinfo: _Optional[str] = ..., src: _Optional[_Union[LogSource, str]] = ...) -> None: ...

class LogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class LogLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class LogSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
