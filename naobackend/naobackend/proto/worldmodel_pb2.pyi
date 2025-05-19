from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
DIRTY: CameraState
OK: CameraState
SAME_PICTURE: CameraState
WDG_TRIGGERED: CameraState

class DebugData(_message.Message):
    __slots__ = ["agent", "order", "stateLowerCam", "stateUpperCam", "teamball", "whistleTimestamp"]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    STATELOWERCAM_FIELD_NUMBER: _ClassVar[int]
    STATEUPPERCAM_FIELD_NUMBER: _ClassVar[int]
    TEAMBALL_FIELD_NUMBER: _ClassVar[int]
    WHISTLETIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    agent: str
    order: Order
    stateLowerCam: CameraState
    stateUpperCam: CameraState
    teamball: Teamball
    whistleTimestamp: int
    def __init__(self, agent: _Optional[str] = ..., order: _Optional[_Union[Order, _Mapping]] = ..., teamball: _Optional[_Union[Teamball, _Mapping]] = ..., whistleTimestamp: _Optional[int] = ..., stateLowerCam: _Optional[_Union[CameraState, str]] = ..., stateUpperCam: _Optional[_Union[CameraState, str]] = ...) -> None: ...

class FirmwareInfo(_message.Message):
    __slots__ = ["currentGcState", "debug", "msgBudget", "penalized", "playerIdx", "teamNumber", "worldmodel"]
    CURRENTGCSTATE_FIELD_NUMBER: _ClassVar[int]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    MSGBUDGET_FIELD_NUMBER: _ClassVar[int]
    PENALIZED_FIELD_NUMBER: _ClassVar[int]
    PLAYERIDX_FIELD_NUMBER: _ClassVar[int]
    TEAMNUMBER_FIELD_NUMBER: _ClassVar[int]
    WORLDMODEL_FIELD_NUMBER: _ClassVar[int]
    currentGcState: int
    debug: DebugData
    msgBudget: int
    penalized: bool
    playerIdx: int
    teamNumber: int
    worldmodel: WorldModel
    def __init__(self, teamNumber: _Optional[int] = ..., playerIdx: _Optional[int] = ..., worldmodel: _Optional[_Union[WorldModel, _Mapping]] = ..., debug: _Optional[_Union[DebugData, _Mapping]] = ..., msgBudget: _Optional[int] = ..., penalized: bool = ..., currentGcState: _Optional[int] = ...) -> None: ...

class Infocast(_message.Message):
    __slots__ = ["debug", "meta", "world"]
    DEBUG_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    WORLD_FIELD_NUMBER: _ClassVar[int]
    debug: DebugData
    meta: RobotMetaInfo
    world: WorldModel
    def __init__(self, meta: _Optional[_Union[RobotMetaInfo, _Mapping]] = ..., world: _Optional[_Union[WorldModel, _Mapping]] = ..., debug: _Optional[_Union[DebugData, _Mapping]] = ...) -> None: ...

class KeepGoalOrder(_message.Message):
    __slots__ = ["allowedToMove"]
    ALLOWEDTOMOVE_FIELD_NUMBER: _ClassVar[int]
    allowedToMove: bool
    def __init__(self, allowedToMove: bool = ...) -> None: ...

class LocationInfo(_message.Message):
    __slots__ = ["a", "qual", "x", "y"]
    A_FIELD_NUMBER: _ClassVar[int]
    QUAL_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    a: float
    qual: float
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., a: _Optional[float] = ..., qual: _Optional[float] = ...) -> None: ...

class MoveBallGoalOrder(_message.Message):
    __slots__ = ["y"]
    Y_FIELD_NUMBER: _ClassVar[int]
    y: float
    def __init__(self, y: _Optional[float] = ...) -> None: ...

class MoveBallOrder(_message.Message):
    __slots__ = ["pos"]
    POS_FIELD_NUMBER: _ClassVar[int]
    pos: Point2D
    def __init__(self, pos: _Optional[_Union[Point2D, _Mapping]] = ...) -> None: ...

class Obstacle(_message.Message):
    __slots__ = ["confindence", "ownTeamProb", "pos"]
    CONFINDENCE_FIELD_NUMBER: _ClassVar[int]
    OWNTEAMPROB_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    confindence: float
    ownTeamProb: float
    pos: Point2D
    def __init__(self, pos: _Optional[_Union[Point2D, _Mapping]] = ..., confindence: _Optional[float] = ..., ownTeamProb: _Optional[float] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ["keepGoalOrder", "moveBallGoalOrder", "moveBallOrder", "name", "walkToPositionOrder"]
    KEEPGOALORDER_FIELD_NUMBER: _ClassVar[int]
    MOVEBALLGOALORDER_FIELD_NUMBER: _ClassVar[int]
    MOVEBALLORDER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    WALKTOPOSITIONORDER_FIELD_NUMBER: _ClassVar[int]
    keepGoalOrder: KeepGoalOrder
    moveBallGoalOrder: MoveBallGoalOrder
    moveBallOrder: MoveBallOrder
    name: str
    walkToPositionOrder: WalkToPositionOrder
    def __init__(self, name: _Optional[str] = ..., moveBallOrder: _Optional[_Union[MoveBallOrder, _Mapping]] = ..., walkToPositionOrder: _Optional[_Union[WalkToPositionOrder, _Mapping]] = ..., moveBallGoalOrder: _Optional[_Union[MoveBallGoalOrder, _Mapping]] = ..., keepGoalOrder: _Optional[_Union[KeepGoalOrder, _Mapping]] = ...) -> None: ...

class Point2D(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ["a", "x", "y"]
    A_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    a: float
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., a: _Optional[float] = ...) -> None: ...

class RelativeBall(_message.Message):
    __slots__ = ["lastSeen", "pos", "speed"]
    LASTSEEN_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    lastSeen: int
    pos: Point2D
    speed: Point2D
    def __init__(self, pos: _Optional[_Union[Point2D, _Mapping]] = ..., speed: _Optional[_Union[Point2D, _Mapping]] = ..., lastSeen: _Optional[int] = ...) -> None: ...

class RobotMetaInfo(_message.Message):
    __slots__ = ["battery", "cpuTemp", "hostname", "lanIp", "lanMac", "wifiIp", "wifiMac", "wifiStrength"]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    CPUTEMP_FIELD_NUMBER: _ClassVar[int]
    HOSTNAME_FIELD_NUMBER: _ClassVar[int]
    LANIP_FIELD_NUMBER: _ClassVar[int]
    LANMAC_FIELD_NUMBER: _ClassVar[int]
    WIFIIP_FIELD_NUMBER: _ClassVar[int]
    WIFIMAC_FIELD_NUMBER: _ClassVar[int]
    WIFISTRENGTH_FIELD_NUMBER: _ClassVar[int]
    battery: int
    cpuTemp: int
    hostname: str
    lanIp: int
    lanMac: bytes
    wifiIp: int
    wifiMac: bytes
    wifiStrength: int
    def __init__(self, hostname: _Optional[str] = ..., battery: _Optional[int] = ..., wifiStrength: _Optional[int] = ..., cpuTemp: _Optional[int] = ..., lanIp: _Optional[int] = ..., lanMac: _Optional[bytes] = ..., wifiIp: _Optional[int] = ..., wifiMac: _Optional[bytes] = ...) -> None: ...

class TeamCommMsg(_message.Message):
    __slots__ = ["ball_age_us", "ball_pos", "has_ball", "is_fallen", "loc_quality", "opponents", "player_idx", "pos", "sent_time", "type"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BALL_AGE_US_FIELD_NUMBER: _ClassVar[int]
    BALL_POS_FIELD_NUMBER: _ClassVar[int]
    GOALIE: TeamCommMsg.Type
    HAS_BALL_FIELD_NUMBER: _ClassVar[int]
    IS_FALLEN_FIELD_NUMBER: _ClassVar[int]
    LOC_QUALITY_FIELD_NUMBER: _ClassVar[int]
    NEW_STRIKER: TeamCommMsg.Type
    NEW_STRIKER_MOVE: TeamCommMsg.Type
    NONE: TeamCommMsg.Type
    OPPONENTS_FIELD_NUMBER: _ClassVar[int]
    OPPONENT_UPDATE: TeamCommMsg.Type
    PLAYER_IDX_FIELD_NUMBER: _ClassVar[int]
    POSITION_UPDATE: TeamCommMsg.Type
    POS_FIELD_NUMBER: _ClassVar[int]
    SENT_TIME_FIELD_NUMBER: _ClassVar[int]
    STRIKER: TeamCommMsg.Type
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ball_age_us: int
    ball_pos: Point2D
    has_ball: bool
    is_fallen: bool
    loc_quality: float
    opponents: _containers.RepeatedCompositeFieldContainer[Obstacle]
    player_idx: int
    pos: Position
    sent_time: int
    type: TeamCommMsg.Type
    def __init__(self, type: _Optional[_Union[TeamCommMsg.Type, str]] = ..., loc_quality: _Optional[float] = ..., player_idx: _Optional[int] = ..., is_fallen: bool = ..., pos: _Optional[_Union[Position, _Mapping]] = ..., has_ball: bool = ..., ball_age_us: _Optional[int] = ..., ball_pos: _Optional[_Union[Point2D, _Mapping]] = ..., opponents: _Optional[_Iterable[_Union[Obstacle, _Mapping]]] = ..., sent_time: _Optional[int] = ...) -> None: ...

class TeamStrategyDebug(_message.Message):
    __slots__ = ["playerToRole", "roleToLocation"]
    class Role(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class PlayerToRoleEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TeamStrategyDebug.Role
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TeamStrategyDebug.Role, str]] = ...) -> None: ...
    class RoleToLocationEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Point2D
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Point2D, _Mapping]] = ...) -> None: ...
    COVER: TeamStrategyDebug.Role
    COVER2: TeamStrategyDebug.Role
    GOALIE: TeamStrategyDebug.Role
    INVALID: TeamStrategyDebug.Role
    MARK: TeamStrategyDebug.Role
    PLAYERTOROLE_FIELD_NUMBER: _ClassVar[int]
    ROLETOLOCATION_FIELD_NUMBER: _ClassVar[int]
    SHADOW: TeamStrategyDebug.Role
    SHADOW2: TeamStrategyDebug.Role
    STRIKER: TeamStrategyDebug.Role
    playerToRole: _containers.ScalarMap[int, TeamStrategyDebug.Role]
    roleToLocation: _containers.MessageMap[int, Point2D]
    def __init__(self, playerToRole: _Optional[_Mapping[int, TeamStrategyDebug.Role]] = ..., roleToLocation: _Optional[_Mapping[int, Point2D]] = ...) -> None: ...

class Teamball(_message.Message):
    __slots__ = ["pos", "qual", "trusted"]
    POS_FIELD_NUMBER: _ClassVar[int]
    QUAL_FIELD_NUMBER: _ClassVar[int]
    TRUSTED_FIELD_NUMBER: _ClassVar[int]
    pos: Point2D
    qual: float
    trusted: bool
    def __init__(self, pos: _Optional[_Union[Point2D, _Mapping]] = ..., qual: _Optional[float] = ..., trusted: bool = ...) -> None: ...

class WalkToPositionOrder(_message.Message):
    __slots__ = ["head_focus", "mode", "obstacles", "pos", "useA"]
    class HeadFocus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class Mode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    FOCUS_BALL: WalkToPositionOrder.HeadFocus
    FOCUS_BALL_GOALIE: WalkToPositionOrder.HeadFocus
    FOCUS_BALL_SEARCH_LEFT: WalkToPositionOrder.HeadFocus
    FOCUS_BALL_SEARCH_RIGHT: WalkToPositionOrder.HeadFocus
    FOCUS_LOC: WalkToPositionOrder.HeadFocus
    FOCUS_NOTHING: WalkToPositionOrder.HeadFocus
    FOCUS_OBSTACLES: WalkToPositionOrder.HeadFocus
    HEAD_FOCUS_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MODE_FOCUS_DIRECTION: WalkToPositionOrder.Mode
    MODE_KEEP_A: WalkToPositionOrder.Mode
    MODE_STRIKER: WalkToPositionOrder.Mode
    MODE_SUPPORTER: WalkToPositionOrder.Mode
    MODE_USE_A: WalkToPositionOrder.Mode
    OBSTACLES_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    USEA_FIELD_NUMBER: _ClassVar[int]
    head_focus: WalkToPositionOrder.HeadFocus
    mode: WalkToPositionOrder.Mode
    obstacles: _containers.RepeatedCompositeFieldContainer[Point2D]
    pos: Position
    useA: bool
    def __init__(self, pos: _Optional[_Union[Position, _Mapping]] = ..., useA: bool = ..., mode: _Optional[_Union[WalkToPositionOrder.Mode, str]] = ..., obstacles: _Optional[_Iterable[_Union[Point2D, _Mapping]]] = ..., head_focus: _Optional[_Union[WalkToPositionOrder.HeadFocus, str]] = ...) -> None: ...

class WorldModel(_message.Message):
    __slots__ = ["ball", "isFallen", "obstacles", "penalized", "pid", "pos", "time"]
    BALL_FIELD_NUMBER: _ClassVar[int]
    ISFALLEN_FIELD_NUMBER: _ClassVar[int]
    OBSTACLES_FIELD_NUMBER: _ClassVar[int]
    PENALIZED_FIELD_NUMBER: _ClassVar[int]
    PID_FIELD_NUMBER: _ClassVar[int]
    POS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    ball: RelativeBall
    isFallen: bool
    obstacles: _containers.RepeatedCompositeFieldContainer[Obstacle]
    penalized: bool
    pid: int
    pos: LocationInfo
    time: int
    def __init__(self, pid: _Optional[int] = ..., time: _Optional[int] = ..., ball: _Optional[_Union[RelativeBall, _Mapping]] = ..., pos: _Optional[_Union[LocationInfo, _Mapping]] = ..., isFallen: bool = ..., penalized: bool = ..., obstacles: _Optional[_Iterable[_Union[Obstacle, _Mapping]]] = ...) -> None: ...

class CameraState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
