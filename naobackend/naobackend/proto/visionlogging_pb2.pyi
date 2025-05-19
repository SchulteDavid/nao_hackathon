from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoundingBox(_message.Message):
    __slots__ = ["a", "b", "prob"]
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    PROB_FIELD_NUMBER: _ClassVar[int]
    a: Point2D
    b: Point2D
    prob: float
    def __init__(self, a: _Optional[_Union[Point2D, _Mapping]] = ..., b: _Optional[_Union[Point2D, _Mapping]] = ..., prob: _Optional[float] = ...) -> None: ...

class CamPose(_message.Message):
    __slots__ = ["body_angles", "body_offset", "cam_id", "ellipse_angles", "head_angles", "head_offset", "leg_height"]
    class CamID(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BODY_ANGLES_FIELD_NUMBER: _ClassVar[int]
    BODY_OFFSET_FIELD_NUMBER: _ClassVar[int]
    CAM_ID_FIELD_NUMBER: _ClassVar[int]
    ELLIPSE_ANGLES_FIELD_NUMBER: _ClassVar[int]
    HEAD_ANGLES_FIELD_NUMBER: _ClassVar[int]
    HEAD_OFFSET_FIELD_NUMBER: _ClassVar[int]
    LEG_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LOWER: CamPose.CamID
    UPPER: CamPose.CamID
    body_angles: YPR
    body_offset: PitchRoll
    cam_id: CamPose.CamID
    ellipse_angles: PitchRoll
    head_angles: YawPitch
    head_offset: PitchRoll
    leg_height: float
    def __init__(self, leg_height: _Optional[float] = ..., body_angles: _Optional[_Union[YPR, _Mapping]] = ..., head_angles: _Optional[_Union[YawPitch, _Mapping]] = ..., cam_id: _Optional[_Union[CamPose.CamID, str]] = ..., body_offset: _Optional[_Union[PitchRoll, _Mapping]] = ..., head_offset: _Optional[_Union[PitchRoll, _Mapping]] = ..., ellipse_angles: _Optional[_Union[PitchRoll, _Mapping]] = ...) -> None: ...

class CenterCirclePoint(_message.Message):
    __slots__ = ["position", "prob", "radius", "x", "y"]
    class CenterCirclePointSide(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    CENTER: CenterCirclePoint.CenterCirclePointSide
    LEFT: CenterCirclePoint.CenterCirclePointSide
    POSITION_FIELD_NUMBER: _ClassVar[int]
    PROB_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    RIGHT: CenterCirclePoint.CenterCirclePointSide
    UNKNOWN: CenterCirclePoint.CenterCirclePointSide
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    position: CenterCirclePoint.CenterCirclePointSide
    prob: float
    radius: int
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., radius: _Optional[int] = ..., prob: _Optional[float] = ..., position: _Optional[_Union[CenterCirclePoint.CenterCirclePointSide, str]] = ...) -> None: ...

class Color(_message.Message):
    __slots__ = ["cb", "cr", "cy"]
    CB_FIELD_NUMBER: _ClassVar[int]
    CR_FIELD_NUMBER: _ClassVar[int]
    CY_FIELD_NUMBER: _ClassVar[int]
    cb: int
    cr: int
    cy: int
    def __init__(self, cy: _Optional[int] = ..., cb: _Optional[int] = ..., cr: _Optional[int] = ...) -> None: ...

class Ellipse(_message.Message):
    __slots__ = ["a", "a1", "b", "b1", "brennpunkt", "c", "c1", "d", "d1", "e", "e1", "f", "f1", "found", "ta", "tb"]
    A1_FIELD_NUMBER: _ClassVar[int]
    A_FIELD_NUMBER: _ClassVar[int]
    B1_FIELD_NUMBER: _ClassVar[int]
    BRENNPUNKT_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    C1_FIELD_NUMBER: _ClassVar[int]
    C_FIELD_NUMBER: _ClassVar[int]
    D1_FIELD_NUMBER: _ClassVar[int]
    D_FIELD_NUMBER: _ClassVar[int]
    E1_FIELD_NUMBER: _ClassVar[int]
    E_FIELD_NUMBER: _ClassVar[int]
    F1_FIELD_NUMBER: _ClassVar[int]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    F_FIELD_NUMBER: _ClassVar[int]
    TA_FIELD_NUMBER: _ClassVar[int]
    TB_FIELD_NUMBER: _ClassVar[int]
    a: float
    a1: float
    b: float
    b1: float
    brennpunkt: float
    c: float
    c1: float
    d: float
    d1: float
    e: float
    e1: float
    f: float
    f1: float
    found: bool
    ta: float
    tb: float
    def __init__(self, a: _Optional[float] = ..., b: _Optional[float] = ..., c: _Optional[float] = ..., d: _Optional[float] = ..., e: _Optional[float] = ..., f: _Optional[float] = ..., a1: _Optional[float] = ..., b1: _Optional[float] = ..., c1: _Optional[float] = ..., d1: _Optional[float] = ..., e1: _Optional[float] = ..., f1: _Optional[float] = ..., ta: _Optional[float] = ..., tb: _Optional[float] = ..., brennpunkt: _Optional[float] = ..., found: bool = ...) -> None: ...

class Feet(_message.Message):
    __slots__ = ["gamma", "left", "right"]
    GAMMA_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    gamma: float
    left: Foot
    right: Foot
    def __init__(self, left: _Optional[_Union[Foot, _Mapping]] = ..., right: _Optional[_Union[Foot, _Mapping]] = ..., gamma: _Optional[float] = ...) -> None: ...

class Foot(_message.Message):
    __slots__ = ["alpha", "beta", "p"]
    ALPHA_FIELD_NUMBER: _ClassVar[int]
    BETA_FIELD_NUMBER: _ClassVar[int]
    P_FIELD_NUMBER: _ClassVar[int]
    alpha: float
    beta: float
    p: Point3Df
    def __init__(self, p: _Optional[_Union[Point3Df, _Mapping]] = ..., alpha: _Optional[float] = ..., beta: _Optional[float] = ...) -> None: ...

class GoalPost(_message.Message):
    __slots__ = ["prob", "radius", "x", "y"]
    PROB_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    prob: float
    radius: int
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., radius: _Optional[int] = ..., prob: _Optional[float] = ...) -> None: ...

class Line(_message.Message):
    __slots__ = ["edges"]
    EDGES_FIELD_NUMBER: _ClassVar[int]
    edges: _containers.RepeatedCompositeFieldContainer[LineEdge]
    def __init__(self, edges: _Optional[_Iterable[_Union[LineEdge, _Mapping]]] = ...) -> None: ...

class LineCross(_message.Message):
    __slots__ = ["px", "py", "vx", "vy"]
    PX_FIELD_NUMBER: _ClassVar[int]
    PY_FIELD_NUMBER: _ClassVar[int]
    VX_FIELD_NUMBER: _ClassVar[int]
    VY_FIELD_NUMBER: _ClassVar[int]
    px: float
    py: float
    vx: float
    vy: float
    def __init__(self, px: _Optional[float] = ..., py: _Optional[float] = ..., vx: _Optional[float] = ..., vy: _Optional[float] = ...) -> None: ...

class LineEdge(_message.Message):
    __slots__ = ["d", "id", "matchCnt", "nx", "ny", "px1", "px2", "py1", "py2", "straight", "valid", "x", "y"]
    D_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    MATCHCNT_FIELD_NUMBER: _ClassVar[int]
    NX_FIELD_NUMBER: _ClassVar[int]
    NY_FIELD_NUMBER: _ClassVar[int]
    PX1_FIELD_NUMBER: _ClassVar[int]
    PX2_FIELD_NUMBER: _ClassVar[int]
    PY1_FIELD_NUMBER: _ClassVar[int]
    PY2_FIELD_NUMBER: _ClassVar[int]
    STRAIGHT_FIELD_NUMBER: _ClassVar[int]
    VALID_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    d: float
    id: int
    matchCnt: int
    nx: float
    ny: float
    px1: float
    px2: float
    py1: float
    py2: float
    straight: bool
    valid: bool
    x: float
    y: float
    def __init__(self, px1: _Optional[float] = ..., px2: _Optional[float] = ..., py1: _Optional[float] = ..., py2: _Optional[float] = ..., nx: _Optional[float] = ..., ny: _Optional[float] = ..., d: _Optional[float] = ..., x: _Optional[float] = ..., y: _Optional[float] = ..., id: _Optional[int] = ..., matchCnt: _Optional[int] = ..., straight: bool = ..., valid: bool = ...) -> None: ...

class LineSegment(_message.Message):
    __slots__ = ["id", "linkX", "linkY", "vx", "vy", "x", "y"]
    ID_FIELD_NUMBER: _ClassVar[int]
    LINKX_FIELD_NUMBER: _ClassVar[int]
    LINKY_FIELD_NUMBER: _ClassVar[int]
    VX_FIELD_NUMBER: _ClassVar[int]
    VY_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    id: int
    linkX: int
    linkY: int
    vx: int
    vy: int
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., vx: _Optional[int] = ..., vy: _Optional[int] = ..., id: _Optional[int] = ..., linkX: _Optional[int] = ..., linkY: _Optional[int] = ...) -> None: ...

class LowerCamObstacleResult(_message.Message):
    __slots__ = ["height", "obstacle", "width"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    OBSTACLE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    height: int
    obstacle: _containers.RepeatedScalarFieldContainer[float]
    width: int
    def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., obstacle: _Optional[_Iterable[float]] = ...) -> None: ...

class ObjectHypotheses(_message.Message):
    __slots__ = ["found", "prob", "radius", "rating", "x", "y"]
    FOUND_FIELD_NUMBER: _ClassVar[int]
    PROB_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    RATING_FIELD_NUMBER: _ClassVar[int]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    found: bool
    prob: float
    radius: int
    rating: float
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., radius: _Optional[int] = ..., prob: _Optional[float] = ..., found: bool = ..., rating: _Optional[float] = ...) -> None: ...

class PitchRoll(_message.Message):
    __slots__ = ["pitch", "roll"]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    pitch: float
    roll: float
    def __init__(self, pitch: _Optional[float] = ..., roll: _Optional[float] = ...) -> None: ...

class Point2D(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: int
    y: int
    def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ...) -> None: ...

class Point2Df(_message.Message):
    __slots__ = ["x", "y"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ...) -> None: ...

class Point3Df(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class RawImage(_message.Message):
    __slots__ = ["cam_id", "image", "reason", "time_us", "vision"]
    CAM_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TIME_US_FIELD_NUMBER: _ClassVar[int]
    VISION_FIELD_NUMBER: _ClassVar[int]
    cam_id: int
    image: bytes
    reason: str
    time_us: int
    vision: VisionFrame
    def __init__(self, vision: _Optional[_Union[VisionFrame, _Mapping]] = ..., image: _Optional[bytes] = ..., time_us: _Optional[int] = ..., cam_id: _Optional[int] = ..., reason: _Optional[str] = ...) -> None: ...

class RobotBoundingBox(_message.Message):
    __slots__ = ["angle", "bb", "dist", "own_team_prob"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    BB_FIELD_NUMBER: _ClassVar[int]
    DIST_FIELD_NUMBER: _ClassVar[int]
    OWN_TEAM_PROB_FIELD_NUMBER: _ClassVar[int]
    angle: float
    bb: BoundingBox
    dist: float
    own_team_prob: float
    def __init__(self, bb: _Optional[_Union[BoundingBox, _Mapping]] = ..., dist: _Optional[float] = ..., angle: _Optional[float] = ..., own_team_prob: _Optional[float] = ...) -> None: ...

class SensorFrame(_message.Message):
    __slots__ = ["accel", "body_pitch", "body_roll", "feet", "gyro", "head_pitch", "head_yaw", "leg_height", "motion_vec", "step_height", "time", "walk_request"]
    ACCEL_FIELD_NUMBER: _ClassVar[int]
    BODY_PITCH_FIELD_NUMBER: _ClassVar[int]
    BODY_ROLL_FIELD_NUMBER: _ClassVar[int]
    FEET_FIELD_NUMBER: _ClassVar[int]
    GYRO_FIELD_NUMBER: _ClassVar[int]
    HEAD_PITCH_FIELD_NUMBER: _ClassVar[int]
    HEAD_YAW_FIELD_NUMBER: _ClassVar[int]
    LEG_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    MOTION_VEC_FIELD_NUMBER: _ClassVar[int]
    STEP_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WALK_REQUEST_FIELD_NUMBER: _ClassVar[int]
    accel: Point3Df
    body_pitch: float
    body_roll: float
    feet: Feet
    gyro: YPR
    head_pitch: float
    head_yaw: float
    leg_height: float
    motion_vec: Point3Df
    step_height: float
    time: int
    walk_request: WalkRequest
    def __init__(self, time: _Optional[int] = ..., head_pitch: _Optional[float] = ..., head_yaw: _Optional[float] = ..., body_pitch: _Optional[float] = ..., body_roll: _Optional[float] = ..., motion_vec: _Optional[_Union[Point3Df, _Mapping]] = ..., gyro: _Optional[_Union[YPR, _Mapping]] = ..., accel: _Optional[_Union[Point3Df, _Mapping]] = ..., leg_height: _Optional[float] = ..., step_height: _Optional[float] = ..., walk_request: _Optional[_Union[WalkRequest, _Mapping]] = ..., feet: _Optional[_Union[Feet, _Mapping]] = ...) -> None: ...

class TinyImage(_message.Message):
    __slots__ = ["height", "u", "v", "width", "y"]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    U_FIELD_NUMBER: _ClassVar[int]
    V_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    height: int
    u: bytes
    v: bytes
    width: int
    y: bytes
    def __init__(self, y: _Optional[bytes] = ..., u: _Optional[bytes] = ..., v: _Optional[bytes] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...

class VisionFrame(_message.Message):
    __slots__ = ["ball", "camPose", "centercirclepoint", "ellipse", "feet", "feets", "fieldBorderY", "fieldColor", "frameId", "goalpost", "height", "lineCrosses", "lineSegments", "lines", "objHypotheses", "obstacle", "penaltySpot", "robots", "time", "tinyImage", "width"]
    BALL_FIELD_NUMBER: _ClassVar[int]
    CAMPOSE_FIELD_NUMBER: _ClassVar[int]
    CENTERCIRCLEPOINT_FIELD_NUMBER: _ClassVar[int]
    ELLIPSE_FIELD_NUMBER: _ClassVar[int]
    FEETS_FIELD_NUMBER: _ClassVar[int]
    FEET_FIELD_NUMBER: _ClassVar[int]
    FIELDBORDERY_FIELD_NUMBER: _ClassVar[int]
    FIELDCOLOR_FIELD_NUMBER: _ClassVar[int]
    FRAMEID_FIELD_NUMBER: _ClassVar[int]
    GOALPOST_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    LINECROSSES_FIELD_NUMBER: _ClassVar[int]
    LINESEGMENTS_FIELD_NUMBER: _ClassVar[int]
    LINES_FIELD_NUMBER: _ClassVar[int]
    OBJHYPOTHESES_FIELD_NUMBER: _ClassVar[int]
    OBSTACLE_FIELD_NUMBER: _ClassVar[int]
    PENALTYSPOT_FIELD_NUMBER: _ClassVar[int]
    ROBOTS_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    TINYIMAGE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    ball: ObjectHypotheses
    camPose: CamPose
    centercirclepoint: _containers.RepeatedCompositeFieldContainer[CenterCirclePoint]
    ellipse: Ellipse
    feet: Point2D
    feets: _containers.RepeatedCompositeFieldContainer[ObjectHypotheses]
    fieldBorderY: _containers.RepeatedScalarFieldContainer[int]
    fieldColor: Color
    frameId: int
    goalpost: _containers.RepeatedCompositeFieldContainer[GoalPost]
    height: int
    lineCrosses: _containers.RepeatedCompositeFieldContainer[LineCross]
    lineSegments: _containers.RepeatedCompositeFieldContainer[LineSegment]
    lines: _containers.RepeatedCompositeFieldContainer[Line]
    objHypotheses: _containers.RepeatedCompositeFieldContainer[ObjectHypotheses]
    obstacle: LowerCamObstacleResult
    penaltySpot: ObjectHypotheses
    robots: _containers.RepeatedCompositeFieldContainer[RobotBoundingBox]
    time: int
    tinyImage: TinyImage
    width: int
    def __init__(self, frameId: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., fieldColor: _Optional[_Union[Color, _Mapping]] = ..., fieldBorderY: _Optional[_Iterable[int]] = ..., lineSegments: _Optional[_Iterable[_Union[LineSegment, _Mapping]]] = ..., lines: _Optional[_Iterable[_Union[Line, _Mapping]]] = ..., ellipse: _Optional[_Union[Ellipse, _Mapping]] = ..., ball: _Optional[_Union[ObjectHypotheses, _Mapping]] = ..., lineCrosses: _Optional[_Iterable[_Union[LineCross, _Mapping]]] = ..., feet: _Optional[_Union[Point2D, _Mapping]] = ..., time: _Optional[int] = ..., penaltySpot: _Optional[_Union[ObjectHypotheses, _Mapping]] = ..., feets: _Optional[_Iterable[_Union[ObjectHypotheses, _Mapping]]] = ..., obstacle: _Optional[_Union[LowerCamObstacleResult, _Mapping]] = ..., camPose: _Optional[_Union[CamPose, _Mapping]] = ..., tinyImage: _Optional[_Union[TinyImage, _Mapping]] = ..., objHypotheses: _Optional[_Iterable[_Union[ObjectHypotheses, _Mapping]]] = ..., goalpost: _Optional[_Iterable[_Union[GoalPost, _Mapping]]] = ..., centercirclepoint: _Optional[_Iterable[_Union[CenterCirclePoint, _Mapping]]] = ..., robots: _Optional[_Iterable[_Union[RobotBoundingBox, _Mapping]]] = ...) -> None: ...

class WalkRequest(_message.Message):
    __slots__ = ["da", "dx", "dy", "shoot"]
    class Shoot(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DA_FIELD_NUMBER: _ClassVar[int]
    DX_FIELD_NUMBER: _ClassVar[int]
    DY_FIELD_NUMBER: _ClassVar[int]
    LEFT: WalkRequest.Shoot
    NONE: WalkRequest.Shoot
    RIGHT: WalkRequest.Shoot
    SHOOT_FIELD_NUMBER: _ClassVar[int]
    da: float
    dx: float
    dy: float
    shoot: WalkRequest.Shoot
    def __init__(self, dx: _Optional[float] = ..., dy: _Optional[float] = ..., da: _Optional[float] = ..., shoot: _Optional[_Union[WalkRequest.Shoot, str]] = ...) -> None: ...

class YPR(_message.Message):
    __slots__ = ["pitch", "roll", "yaw"]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    pitch: float
    roll: float
    yaw: float
    def __init__(self, yaw: _Optional[float] = ..., pitch: _Optional[float] = ..., roll: _Optional[float] = ...) -> None: ...

class YawPitch(_message.Message):
    __slots__ = ["pitch", "yaw"]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    pitch: float
    yaw: float
    def __init__(self, yaw: _Optional[float] = ..., pitch: _Optional[float] = ...) -> None: ...
