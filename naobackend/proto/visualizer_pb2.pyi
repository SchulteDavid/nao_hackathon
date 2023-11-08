from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

ABSOLUTE: VisualizerTransactionType
DESCRIPTOR: _descriptor.FileDescriptor
NO_REPLACE: VisualizerReplacement
RELATIVE_BODY: VisualizerTransactionType
RELATIVE_HEAD: VisualizerTransactionType
REPLACE: VisualizerReplacement

class Arc2D(_message.Message):
    __slots__ = ["arcAngle", "borderColor", "centerX", "centerY", "fadingTime", "fillColor", "height", "startAngle", "type", "width"]
    class Arc2DType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ARCANGLE_FIELD_NUMBER: _ClassVar[int]
    BORDERCOLOR_FIELD_NUMBER: _ClassVar[int]
    CENTERX_FIELD_NUMBER: _ClassVar[int]
    CENTERY_FIELD_NUMBER: _ClassVar[int]
    CHORD: Arc2D.Arc2DType
    FADINGTIME_FIELD_NUMBER: _ClassVar[int]
    FILLCOLOR_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    OPEN: Arc2D.Arc2DType
    PIE: Arc2D.Arc2DType
    STARTANGLE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    arcAngle: float
    borderColor: Color
    centerX: float
    centerY: float
    fadingTime: int
    fillColor: Color
    height: float
    startAngle: float
    type: Arc2D.Arc2DType
    width: float
    def __init__(self, borderColor: _Optional[_Union[Color, _Mapping]] = ..., fillColor: _Optional[_Union[Color, _Mapping]] = ..., fadingTime: _Optional[int] = ..., centerX: _Optional[float] = ..., centerY: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ..., startAngle: _Optional[float] = ..., arcAngle: _Optional[float] = ..., type: _Optional[_Union[Arc2D.Arc2DType, str]] = ...) -> None: ...

class Color(_message.Message):
    __slots__ = ["a", "b", "g", "r"]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    G_FIELD_NUMBER: _ClassVar[int]
    R_FIELD_NUMBER: _ClassVar[int]
    a: int
    b: int
    g: int
    r: int
    def __init__(self, r: _Optional[int] = ..., g: _Optional[int] = ..., b: _Optional[int] = ..., a: _Optional[int] = ...) -> None: ...

class Ellipsis2D(_message.Message):
    __slots__ = ["angle", "borderColor", "centerX", "centerY", "fadingTime", "fillColor", "height", "width"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    BORDERCOLOR_FIELD_NUMBER: _ClassVar[int]
    CENTERX_FIELD_NUMBER: _ClassVar[int]
    CENTERY_FIELD_NUMBER: _ClassVar[int]
    FADINGTIME_FIELD_NUMBER: _ClassVar[int]
    FILLCOLOR_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    angle: float
    borderColor: Color
    centerX: float
    centerY: float
    fadingTime: int
    fillColor: Color
    height: float
    width: float
    def __init__(self, borderColor: _Optional[_Union[Color, _Mapping]] = ..., fillColor: _Optional[_Union[Color, _Mapping]] = ..., fadingTime: _Optional[int] = ..., centerX: _Optional[float] = ..., centerY: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ..., angle: _Optional[float] = ...) -> None: ...

class Head(_message.Message):
    __slots__ = ["pitch", "yaw"]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    pitch: float
    yaw: float
    def __init__(self, yaw: _Optional[float] = ..., pitch: _Optional[float] = ...) -> None: ...

class Line2D(_message.Message):
    __slots__ = ["color", "fadingTime", "type", "x1", "x2", "y1", "y2"]
    class LineType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ARROW: Line2D.LineType
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FADINGTIME_FIELD_NUMBER: _ClassVar[int]
    NORMAL: Line2D.LineType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    X1_FIELD_NUMBER: _ClassVar[int]
    X2_FIELD_NUMBER: _ClassVar[int]
    Y1_FIELD_NUMBER: _ClassVar[int]
    Y2_FIELD_NUMBER: _ClassVar[int]
    color: Color
    fadingTime: int
    type: Line2D.LineType
    x1: float
    x2: float
    y1: float
    y2: float
    def __init__(self, color: _Optional[_Union[Color, _Mapping]] = ..., fadingTime: _Optional[int] = ..., x1: _Optional[float] = ..., y1: _Optional[float] = ..., x2: _Optional[float] = ..., y2: _Optional[float] = ..., type: _Optional[_Union[Line2D.LineType, str]] = ...) -> None: ...

class Parameter(_message.Message):
    __slots__ = ["color", "floatParams", "intParams", "name"]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FLOATPARAMS_FIELD_NUMBER: _ClassVar[int]
    INTPARAMS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    color: Color
    floatParams: _containers.RepeatedScalarFieldContainer[float]
    intParams: _containers.RepeatedScalarFieldContainer[int]
    name: str
    def __init__(self, name: _Optional[str] = ..., intParams: _Optional[_Iterable[int]] = ..., floatParams: _Optional[_Iterable[float]] = ..., color: _Optional[_Union[Color, _Mapping]] = ...) -> None: ...

class Raster2D(_message.Message):
    __slots__ = ["color", "data", "fadingTime", "height", "rotation", "scale", "width", "x", "y"]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    FADINGTIME_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ROTATION_FIELD_NUMBER: _ClassVar[int]
    SCALE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    color: Color
    data: _containers.RepeatedScalarFieldContainer[int]
    fadingTime: int
    height: int
    rotation: float
    scale: float
    width: int
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., rotation: _Optional[float] = ..., scale: _Optional[float] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., color: _Optional[_Union[Color, _Mapping]] = ..., fadingTime: _Optional[int] = ..., data: _Optional[_Iterable[int]] = ...) -> None: ...

class Rectangle2D(_message.Message):
    __slots__ = ["borderColor", "fadingTime", "fillColor", "height", "upperLeftX", "upperLeftY", "width"]
    BORDERCOLOR_FIELD_NUMBER: _ClassVar[int]
    FADINGTIME_FIELD_NUMBER: _ClassVar[int]
    FILLCOLOR_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    UPPERLEFTX_FIELD_NUMBER: _ClassVar[int]
    UPPERLEFTY_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    borderColor: Color
    fadingTime: int
    fillColor: Color
    height: float
    upperLeftX: float
    upperLeftY: float
    width: float
    def __init__(self, borderColor: _Optional[_Union[Color, _Mapping]] = ..., fillColor: _Optional[_Union[Color, _Mapping]] = ..., fadingTime: _Optional[int] = ..., upperLeftX: _Optional[float] = ..., upperLeftY: _Optional[float] = ..., width: _Optional[float] = ..., height: _Optional[float] = ...) -> None: ...

class Text2D(_message.Message):
    __slots__ = ["color", "fadingTime", "size", "text", "x", "y"]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    FADINGTIME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    color: Color
    fadingTime: int
    size: float
    text: str
    x: float
    y: float
    def __init__(self, color: _Optional[_Union[Color, _Mapping]] = ..., fadingTime: _Optional[int] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., size: _Optional[float] = ..., text: _Optional[str] = ...) -> None: ...

class VisualizerTransaction(_message.Message):
    __slots__ = ["arcs", "ellipses", "head", "lines", "messages", "parameter", "raster", "rectangles", "replacement", "subsystem", "texts", "time", "transactionType"]
    ARCS_FIELD_NUMBER: _ClassVar[int]
    ELLIPSES_FIELD_NUMBER: _ClassVar[int]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    RASTER_FIELD_NUMBER: _ClassVar[int]
    RECTANGLES_FIELD_NUMBER: _ClassVar[int]
    REPLACEMENT_FIELD_NUMBER: _ClassVar[int]
    SUBSYSTEM_FIELD_NUMBER: _ClassVar[int]
    TEXTS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONTYPE_FIELD_NUMBER: _ClassVar[int]
    arcs: _containers.RepeatedCompositeFieldContainer[Arc2D]
    ellipses: _containers.RepeatedCompositeFieldContainer[Ellipsis2D]
    head: Head
    lines: _containers.RepeatedCompositeFieldContainer[Line2D]
    messages: _containers.RepeatedScalarFieldContainer[str]
    parameter: _containers.RepeatedCompositeFieldContainer[Parameter]
    raster: _containers.RepeatedCompositeFieldContainer[Raster2D]
    rectangles: _containers.RepeatedCompositeFieldContainer[Rectangle2D]
    replacement: VisualizerReplacement
    subsystem: str
    texts: _containers.RepeatedCompositeFieldContainer[Text2D]
    time: int
    transactionType: VisualizerTransactionType
    def __init__(self, replacement: _Optional[_Union[VisualizerReplacement, str]] = ..., transactionType: _Optional[_Union[VisualizerTransactionType, str]] = ..., time: _Optional[int] = ..., subsystem: _Optional[str] = ..., messages: _Optional[_Iterable[str]] = ..., head: _Optional[_Union[Head, _Mapping]] = ..., parameter: _Optional[_Iterable[_Union[Parameter, _Mapping]]] = ..., lines: _Optional[_Iterable[_Union[Line2D, _Mapping]]] = ..., ellipses: _Optional[_Iterable[_Union[Ellipsis2D, _Mapping]]] = ..., rectangles: _Optional[_Iterable[_Union[Rectangle2D, _Mapping]]] = ..., arcs: _Optional[_Iterable[_Union[Arc2D, _Mapping]]] = ..., texts: _Optional[_Iterable[_Union[Text2D, _Mapping]]] = ..., raster: _Optional[_Iterable[_Union[Raster2D, _Mapping]]] = ...) -> None: ...

class VisualizerTransactionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class VisualizerReplacement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
