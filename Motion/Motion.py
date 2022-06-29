from naoqi import ALProxy

#http://doc.aldebaran.com/2-1/naoqi/motion/almotion-api.html
class Motion:
    def __init__(self, ip, port):
        self.proxy = ALProxy("ALMotion", ip, port)

    """
    this method is part of the Join Control Api
    http://doc.aldebaran.com/2-1/naoqi/motion/control-joint-api.html#control-joint-api
    it can be used to get current angle of certain joints. http://doc.aldebaran.com/2-1/family/robots/bodyparts.html#effector-chain
    receives the name of the Joint and if the sensors should be used or not
    Through experimentation, it was found that the measurements were more precise without using the sensors.
    Returns an array of float, which are all in radians.
    """

    def get_horizontal_head_angle(self):
        joint_name = "Head"
        use_sensors = False
        return self.proxy.getAngles(joint_name, use_sensors)[0]

    """
    This is based of an example in the documentation, it moves the robot according to its axis
    x: Meters
    y: Meters
    Theta: Radians [-3.1415 to 3.1415]
    """

    def walk(self, x, y, Theta):
        # Enable Arm movemment
        # Lets the arms be controlled by the Walk task
        # Disabling any of this will likely cause the robot to fall
        # left | right its the order of the params
        self.proxy.setWalkArmsEnabled(True, True)
        # General Api
        self.proxy.setMotionConfig([["ENABLE_FOOT_CONTACT_PROTECTION", True]])

        # Its possible to use the almath library to get the 2D position and calculate the movement

        self.proxy.post.moveTo(x, y, Theta)
        # wait is useful because with post moveTo is not blocking function
        # self.proxy.waitUntilMoveIsFinished()
