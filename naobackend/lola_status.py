from dataclasses import dataclass
from enum import Enum

from naobackend.proto import lola_lowlevel_pb2


@dataclass
class JointRead:
    angle: float
    current: float
    temperature: float
    stiffness: float
    status: float


@dataclass
class JointWrite:
    angle: float
    stiffness: float


@dataclass
class Joint:
    read: JointRead
    write: JointWrite


@dataclass
class YPRJoint:
    yaw: Joint
    pitch: Joint
    roll: Joint


@dataclass
class YPJoint:
    yaw: Joint
    pitch: Joint


@dataclass
class PRJoint:
    pitch: Joint
    roll: Joint


@dataclass
class YRJoint:
    yaw: Joint
    roll: Joint


@dataclass
class YPR:
    yaw: float
    pitch: float
    roll: float


@dataclass
class Point3d:
    x: float
    y: float
    z: float


class Shoot(Enum):
    NONE = 0
    LEFT = 1
    RIGHT = 2


@dataclass
class WalkRequest:
    dx: float
    dy: float
    da: float
    shoot: Shoot
    foot_v_angle: float


@dataclass
class HeadRequest:
    yaw: JointWrite
    pitch: JointWrite


@dataclass
class IMU:
    gyro: YPR
    accel: Point3d


@dataclass
class BodySide:
    shoulder: PRJoint
    elbow: YRJoint
    hip: PRJoint
    knee_pitch: Joint
    ankle: PRJoint
    wrist_yaw: Joint
    hand: Joint


@dataclass
class RobotJoints:
    head: YPJoint
    hip_yaw: Joint
    left: BodySide
    right: BodySide


@dataclass
class Battery:
    current: float
    temp: float
    status: float
    charge: float


@dataclass
class FootFSR:
    fl: float
    fr: float
    rl: float
    rr: float


@dataclass
class FSR:
    left: FootFSR
    right: FootFSR


@dataclass
class LolaStatus:
    timestamp: int
    walkrequest: WalkRequest
    headrequest: HeadRequest
    joints: RobotJoints
    battery: Battery
    imu: IMU
    fsr: FSR

    def flatten(self) -> dict[str, float]:
        r = dict()

        def joint_write(prefix: str, j: JointWrite) -> dict[str,float]:
            d = dict()
            d[f'{prefix}.angle'] = j.angle
            d[f'{prefix}.stiffness'] = j.stiffness
            return d

        def joint_read(prefix: str, j: JointRead) -> dict[str, float]:
            d = dict()
            d[f'{prefix}.angle'] = j.angle
            d[f'{prefix}.current'] = j.current
            d[f'{prefix}.temperature'] = j.temperature
            d[f'{prefix}.stiffness'] = j.stiffness
            d[f'{prefix}.status'] = j.status
            return d

        def joint(prefix: str, j: Joint):
            d = joint_read(prefix + ".read", j.read)
            d = d | joint_write(prefix + ".write", j.write)
            return d

        r['timestamp'] = self.timestamp
        r['walkrequest.dx'] = self.walkrequest.dx
        r['walkrequest.dy'] = self.walkrequest.dy
        r['walkrequest.da'] = self.walkrequest.da
        r['walkrequest.foot_v_angle'] = self.walkrequest.foot_v_angle

        if self.walkrequest.shoot == Shoot.LEFT:
            r['walkrequest.shoot'] = 'left'
        elif self.walkrequest.shoot == Shoot.RIGHT:
            r['walkrequest.shoot'] = 'right'
        else:
            r['walkrequest.shoot'] = 'none'

        r = r | joint_write('headrequest.yaw', self.headrequest.yaw)
        r = r | joint_write('headrequest.pitch', self.headrequest.pitch)

        r = r | joint('joints.head.yaw', self.joints.head.yaw)
        r = r | joint('joints.head.pitch', self.joints.head.pitch)
        r = r | joint('joints.head_yaw', self.joints.hip_yaw)
        r = r | joint('joints.left.shoulder.pitch', self.joints.left.shoulder.pitch)
        r = r | joint('joints.left.shoulder.roll', self.joints.left.shoulder.roll)
        r = r | joint('joints.left.elbow.yaw', self.joints.left.elbow.yaw)
        r = r | joint('joints.left.elbow.roll', self.joints.left.elbow.roll)
        r = r | joint('joints.left.hip.pitch', self.joints.left.hip.pitch)
        r = r | joint('joints.left.hip.roll', self.joints.left.hip.roll)
        r = r | joint('joints.left.knee_pitch', self.joints.left.knee_pitch)
        r = r | joint('joints.left.ankle.pitch', self.joints.left.ankle.pitch)
        r = r | joint('joints.left.ankle.roll', self.joints.left.ankle.roll)
        r = r | joint('joints.left.wrist_yaw', self.joints.left.wrist_yaw)
        r = r | joint('joints.left.hand', self.joints.left.hand)

        r = r | joint('joints.right.shoulder.pitch', self.joints.right.shoulder.pitch)
        r = r | joint('joints.right.shoulder.roll', self.joints.right.shoulder.roll)
        r = r | joint('joints.right.elbow.yaw', self.joints.right.elbow.yaw)
        r = r | joint('joints.right.elbow.roll', self.joints.right.elbow.roll)
        r = r | joint('joints.right.hip.pitch', self.joints.right.hip.pitch)
        r = r | joint('joints.right.hip.roll', self.joints.right.hip.roll)
        r = r | joint('joints.right.knee_pitch', self.joints.right.knee_pitch)
        r = r | joint('joints.right.ankle.pitch', self.joints.right.ankle.pitch)
        r = r | joint('joints.right.ankle.roll', self.joints.right.ankle.roll)
        r = r | joint('joints.right.wrist_yaw', self.joints.right.wrist_yaw)
        r = r | joint('joints.right.hand', self.joints.right.hand)

        r['battery.status'] = self.battery.status
        r['battery.current'] = self.battery.current
        r['battery.temp'] = self.battery.temp
        r['battery.charge'] = self.battery.charge

        r['fsr.left.fl'] = self.fsr.left.fl
        r['fsr.left.fr'] = self.fsr.left.fr
        r['fsr.left.rl'] = self.fsr.left.rl
        r['fsr.left.rr'] = self.fsr.left.rr

        r['fsr.right.fl'] = self.fsr.right.fl
        r['fsr.right.fr'] = self.fsr.right.fr
        r['fsr.right.rl'] = self.fsr.right.rl
        r['fsr.right.rr'] = self.fsr.right.rr

        r['imu.gyro.yaw'] = self.imu.gyro.yaw
        r['imu.gyro.pitch'] = self.imu.gyro.pitch
        r['imu.gyro.roll'] = self.imu.gyro.roll
        r['imu.accel.x'] = self.imu.accel.x
        r['imu.accel.y'] = self.imu.accel.y
        r['imu.accel.z'] = self.imu.accel.z

        return r



def _joint_read(l: lola_lowlevel_pb2.JointRead) -> JointRead:
    return JointRead(l.angle, l.current, l.temperature, l.stiffness, l.status)


def _joint_write(j: lola_lowlevel_pb2.JointWrite) -> JointWrite:
    return JointWrite(j.angle, j.stiffness)


def _joint(j: lola_lowlevel_pb2.Joint) -> Joint:
    return Joint(_joint_read(j.read), _joint_write(j.write))


def _ypr_joint(j: lola_lowlevel_pb2.YPRJoint) -> YPRJoint:
    return YPRJoint(_joint(j.yaw), _joint(j.pitch), _joint(j.roll))


def _yp_joint(j: lola_lowlevel_pb2.YPJoint) -> YPJoint:
    return YPJoint(_joint(j.yaw), _joint(j.pitch))


def _pr_joint(j: lola_lowlevel_pb2.PRJoint) -> PRJoint:
    return PRJoint(_joint(j.pitch), _joint(j.roll))


def _yr_joint(j: lola_lowlevel_pb2.YRJoint) -> YRJoint:
    return YRJoint(_joint(j.yaw), _joint(j.roll))


def _bodyside(bside: lola_lowlevel_pb2.BodySide) -> BodySide:
    return BodySide(
        shoulder=_pr_joint(bside.shoulder),
        elbow=_yr_joint(bside.elbow),
        hip=_pr_joint(bside.hip),
        knee_pitch=_joint(bside.knee_pitch),
        ankle=_pr_joint(bside.ankle),
        wrist_yaw=_joint(bside.wrist_yaw),
        hand=_joint(bside.hand),
    )


def convert_from_proto(lola_status_proto: lola_lowlevel_pb2.LolaStatus) -> LolaStatus:
    l = lola_status_proto

    timestamp = l.timestamp

    robot_joints = RobotJoints(head=_yp_joint(l.joints.head), hip_yaw=_joint(l.joints.hip_yaw),
                               left=_bodyside(l.joints.left), right=_bodyside(l.joints.right))

    walk_request = WalkRequest(l.walkrequest.dx, l.walkrequest.dy, l.walkrequest.da, l.walkrequest.shoot,
                               l.walkrequest.foot_v_angle)

    head_request_yaw = JointWrite(l.headrequest.yaw.angle, l.headrequest.yaw.stiffness)
    head_request_pitch = JointWrite(l.headrequest.pitch.angle, l.headrequest.pitch.stiffness)
    head_request = HeadRequest(head_request_yaw, head_request_pitch)

    gyro = YPR(l.imu.gyro.yaw, l.imu.gyro.pitch, l.imu.gyro.roll)
    accel = Point3d(l.imu.accel.x, l.imu.accel.y, l.imu.accel.z)
    imu = IMU(gyro, accel)

    battery = Battery(l.battery.current, l.battery.temp, l.battery.status, l.battery.charge)

    fsr_left = FootFSR(l.fsr.left.fl, l.fsr.left.fr, l.fsr.left.rl, l.fsr.left.rr)
    fsr_right = FootFSR(l.fsr.right.fl, l.fsr.right.fr, l.fsr.right.rl, l.fsr.right.rr)
    fsr = FSR(fsr_left, fsr_right)

    return LolaStatus(timestamp, walk_request, head_request, robot_joints, battery, imu, fsr)
