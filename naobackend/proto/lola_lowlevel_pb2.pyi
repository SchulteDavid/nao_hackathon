from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Battery(_message.Message):
    __slots__ = ["charge", "current", "status", "temp"]
    CHARGE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TEMP_FIELD_NUMBER: _ClassVar[int]
    charge: float
    current: float
    status: float
    temp: float
    def __init__(self, current: _Optional[float] = ..., temp: _Optional[float] = ..., status: _Optional[float] = ..., charge: _Optional[float] = ...) -> None: ...

class BodySide(_message.Message):
    __slots__ = ["ankle", "elbow", "hand", "hip", "knee_pitch", "shoulder", "wrist_yaw"]
    ANKLE_FIELD_NUMBER: _ClassVar[int]
    ELBOW_FIELD_NUMBER: _ClassVar[int]
    HAND_FIELD_NUMBER: _ClassVar[int]
    HIP_FIELD_NUMBER: _ClassVar[int]
    KNEE_PITCH_FIELD_NUMBER: _ClassVar[int]
    SHOULDER_FIELD_NUMBER: _ClassVar[int]
    WRIST_YAW_FIELD_NUMBER: _ClassVar[int]
    ankle: PRJoint
    elbow: YRJoint
    hand: Joint
    hip: PRJoint
    knee_pitch: Joint
    shoulder: PRJoint
    wrist_yaw: Joint
    def __init__(self, shoulder: _Optional[_Union[PRJoint, _Mapping]] = ..., elbow: _Optional[_Union[YRJoint, _Mapping]] = ..., hip: _Optional[_Union[PRJoint, _Mapping]] = ..., knee_pitch: _Optional[_Union[Joint, _Mapping]] = ..., ankle: _Optional[_Union[PRJoint, _Mapping]] = ..., wrist_yaw: _Optional[_Union[Joint, _Mapping]] = ..., hand: _Optional[_Union[Joint, _Mapping]] = ...) -> None: ...

class FSR(_message.Message):
    __slots__ = ["left", "right"]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    left: FootFSR
    right: FootFSR
    def __init__(self, left: _Optional[_Union[FootFSR, _Mapping]] = ..., right: _Optional[_Union[FootFSR, _Mapping]] = ...) -> None: ...

class FootFSR(_message.Message):
    __slots__ = ["fl", "fr", "rl", "rr"]
    FL_FIELD_NUMBER: _ClassVar[int]
    FR_FIELD_NUMBER: _ClassVar[int]
    RL_FIELD_NUMBER: _ClassVar[int]
    RR_FIELD_NUMBER: _ClassVar[int]
    fl: float
    fr: float
    rl: float
    rr: float
    def __init__(self, fl: _Optional[float] = ..., fr: _Optional[float] = ..., rl: _Optional[float] = ..., rr: _Optional[float] = ...) -> None: ...

class HeadRequest(_message.Message):
    __slots__ = ["pitch", "yaw"]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    pitch: JointWrite
    yaw: JointWrite
    def __init__(self, yaw: _Optional[_Union[JointWrite, _Mapping]] = ..., pitch: _Optional[_Union[JointWrite, _Mapping]] = ...) -> None: ...

class IMU(_message.Message):
    __slots__ = ["accel", "gyro"]
    ACCEL_FIELD_NUMBER: _ClassVar[int]
    GYRO_FIELD_NUMBER: _ClassVar[int]
    accel: Point3D
    gyro: YPR
    def __init__(self, gyro: _Optional[_Union[YPR, _Mapping]] = ..., accel: _Optional[_Union[Point3D, _Mapping]] = ...) -> None: ...

class Joint(_message.Message):
    __slots__ = ["read", "write"]
    READ_FIELD_NUMBER: _ClassVar[int]
    WRITE_FIELD_NUMBER: _ClassVar[int]
    read: JointRead
    write: JointWrite
    def __init__(self, read: _Optional[_Union[JointRead, _Mapping]] = ..., write: _Optional[_Union[JointWrite, _Mapping]] = ...) -> None: ...

class JointRead(_message.Message):
    __slots__ = ["angle", "current", "status", "stiffness", "temperature"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STIFFNESS_FIELD_NUMBER: _ClassVar[int]
    TEMPERATURE_FIELD_NUMBER: _ClassVar[int]
    angle: float
    current: float
    status: int
    stiffness: float
    temperature: float
    def __init__(self, angle: _Optional[float] = ..., current: _Optional[float] = ..., temperature: _Optional[float] = ..., stiffness: _Optional[float] = ..., status: _Optional[int] = ...) -> None: ...

class JointWrite(_message.Message):
    __slots__ = ["angle", "stiffness"]
    ANGLE_FIELD_NUMBER: _ClassVar[int]
    STIFFNESS_FIELD_NUMBER: _ClassVar[int]
    angle: float
    stiffness: float
    def __init__(self, angle: _Optional[float] = ..., stiffness: _Optional[float] = ...) -> None: ...

class LolaStatus(_message.Message):
    __slots__ = ["battery", "fsr", "headrequest", "imu", "joints", "timestamp", "walkrequest"]
    BATTERY_FIELD_NUMBER: _ClassVar[int]
    FSR_FIELD_NUMBER: _ClassVar[int]
    HEADREQUEST_FIELD_NUMBER: _ClassVar[int]
    IMU_FIELD_NUMBER: _ClassVar[int]
    JOINTS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    WALKREQUEST_FIELD_NUMBER: _ClassVar[int]
    battery: Battery
    fsr: FSR
    headrequest: HeadRequest
    imu: IMU
    joints: RobotJoints
    timestamp: int
    walkrequest: WalkRequest
    def __init__(self, timestamp: _Optional[int] = ..., walkrequest: _Optional[_Union[WalkRequest, _Mapping]] = ..., headrequest: _Optional[_Union[HeadRequest, _Mapping]] = ..., joints: _Optional[_Union[RobotJoints, _Mapping]] = ..., battery: _Optional[_Union[Battery, _Mapping]] = ..., imu: _Optional[_Union[IMU, _Mapping]] = ..., fsr: _Optional[_Union[FSR, _Mapping]] = ...) -> None: ...

class PRJoint(_message.Message):
    __slots__ = ["pitch", "roll"]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    pitch: Joint
    roll: Joint
    def __init__(self, pitch: _Optional[_Union[Joint, _Mapping]] = ..., roll: _Optional[_Union[Joint, _Mapping]] = ...) -> None: ...

class Point3D(_message.Message):
    __slots__ = ["x", "y", "z"]
    X_FIELD_NUMBER: _ClassVar[int]
    Y_FIELD_NUMBER: _ClassVar[int]
    Z_FIELD_NUMBER: _ClassVar[int]
    x: float
    y: float
    z: float
    def __init__(self, x: _Optional[float] = ..., y: _Optional[float] = ..., z: _Optional[float] = ...) -> None: ...

class RobotJoints(_message.Message):
    __slots__ = ["head", "hip_yaw", "left", "right"]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    HIP_YAW_FIELD_NUMBER: _ClassVar[int]
    LEFT_FIELD_NUMBER: _ClassVar[int]
    RIGHT_FIELD_NUMBER: _ClassVar[int]
    head: YPJoint
    hip_yaw: Joint
    left: BodySide
    right: BodySide
    def __init__(self, head: _Optional[_Union[YPJoint, _Mapping]] = ..., hip_yaw: _Optional[_Union[Joint, _Mapping]] = ..., left: _Optional[_Union[BodySide, _Mapping]] = ..., right: _Optional[_Union[BodySide, _Mapping]] = ...) -> None: ...

class WalkRequest(_message.Message):
    __slots__ = ["da", "dx", "dy", "foot_v_angle", "shoot"]
    class Shoot(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    DA_FIELD_NUMBER: _ClassVar[int]
    DX_FIELD_NUMBER: _ClassVar[int]
    DY_FIELD_NUMBER: _ClassVar[int]
    FOOT_V_ANGLE_FIELD_NUMBER: _ClassVar[int]
    LEFT: WalkRequest.Shoot
    NONE: WalkRequest.Shoot
    RIGHT: WalkRequest.Shoot
    SHOOT_FIELD_NUMBER: _ClassVar[int]
    da: float
    dx: float
    dy: float
    foot_v_angle: float
    shoot: WalkRequest.Shoot
    def __init__(self, dx: _Optional[float] = ..., dy: _Optional[float] = ..., da: _Optional[float] = ..., shoot: _Optional[_Union[WalkRequest.Shoot, str]] = ..., foot_v_angle: _Optional[float] = ...) -> None: ...

class YPJoint(_message.Message):
    __slots__ = ["pitch", "yaw"]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    pitch: Joint
    yaw: Joint
    def __init__(self, yaw: _Optional[_Union[Joint, _Mapping]] = ..., pitch: _Optional[_Union[Joint, _Mapping]] = ...) -> None: ...

class YPR(_message.Message):
    __slots__ = ["pitch", "roll", "yaw"]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    pitch: float
    roll: float
    yaw: float
    def __init__(self, yaw: _Optional[float] = ..., pitch: _Optional[float] = ..., roll: _Optional[float] = ...) -> None: ...

class YPRJoint(_message.Message):
    __slots__ = ["pitch", "roll", "yaw"]
    PITCH_FIELD_NUMBER: _ClassVar[int]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    pitch: Joint
    roll: Joint
    yaw: Joint
    def __init__(self, yaw: _Optional[_Union[Joint, _Mapping]] = ..., pitch: _Optional[_Union[Joint, _Mapping]] = ..., roll: _Optional[_Union[Joint, _Mapping]] = ...) -> None: ...

class YRJoint(_message.Message):
    __slots__ = ["roll", "yaw"]
    ROLL_FIELD_NUMBER: _ClassVar[int]
    YAW_FIELD_NUMBER: _ClassVar[int]
    roll: Joint
    yaw: Joint
    def __init__(self, yaw: _Optional[_Union[Joint, _Mapping]] = ..., roll: _Optional[_Union[Joint, _Mapping]] = ...) -> None: ...
