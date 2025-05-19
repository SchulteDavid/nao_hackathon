import naobackend.robot_option_connection as roptions


class WalkControl:
    def __init__(self, ip):
        # Connect to robot
        self.robot = roptions.RobotOptionConnection()
        self.robot.connect(ip)
        self.walk_tuner = self.robot.firmware_options.option_sets["walktuner"]
        self.param_tuner = self.robot.bridge_options.option_sets["walkingengine"]
        # self.param_tuner2 = self.robot.bridge_options.option_sets["anklebalancer"]

        self.WALK_STAND = 0
        self.WALK_RELATIVE = 1
        self.WALK_ABSOLUTE = 2
        self.WALK_SIT = 3

    def set_velocity(self, vx, vy, va):
        # We want to move relative. So we set first the direction and then the mode
        if vx == 0 and vy == 0 and va == 0:
            self.walk_tuner.options["mode"].value = self.WALK_STAND
            #self.walk_tuner.options["timeout_ms"].value = 0
        else:
            self.walk_tuner.options["vx"].value = vx
            self.walk_tuner.options["vy"].value = vy
            self.walk_tuner.options["va"].value = va
            self.walk_tuner.options["mode"].value = self.WALK_RELATIVE
            #self.walk_tuner.options["timeout_ms"].value = 60000

    def set_target(self, x, y, a):
        # We want to move to a absolute position.
        self.walk_tuner.options["abs_x"].value = x
        self.walk_tuner.options["abs_y"].value = y
        self.walk_tuner.options["abs_a"].value = a
        self.walk_tuner.options["abs_allowed_delta"].value = 0.2  # Delta in meter where we stop and stand -> reset mode to 0
        self.walk_tuner.options["mode"].value = self.WALK_ABSOLUTE
        # self.walk_tuner.options["timeout_ms"].value = 30000

    def set_sit(self, sit):
        # We want to move to a absolute position.
        if sit:
            self.walk_tuner.options["mode"].value = self.WALK_SIT
        else:
            self.walk_tuner.options["mode"].value = self.WALK_STAND

    def set_param(self, group, name, value):
        if group == "walkingengine":
            self.param_tuner.options[name].value = value
        if group == "anklebalancer":
            self.param_tuner2.options[name].value = value

    def set_params(self, params):
        for pname, value in params.items():
            group, name = pname.split(".")
            self.set_param(group, name, value)