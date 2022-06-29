

#http://doc.aldebaran.com/2-1/naoqi/motion/alrobotposture.html#alrobotposture
"""
    List of postures:
    Crouch
    LyingBack
    LyingBelly
    Sit
    SitRelax
    Stand
    StandInit
    StandZero
"""
from naoqi import ALProxy


class Posture:
    def _init_(self, ip, port):
        self.proxy = ALProxy("ALRobotPosture", ip, port)

    """
    set the posture of the robot
    receives the name of the posture
    Its a blocking call, meaning the robot will not be able to do anything else, while changing posture
    """
    def set_posture(self, posture_name):
        speed = 0.5 #speed of movement goes from [0,1]
        """
        The apply posture its a faster and less secure way, since it has no intelligence
        it will only try and reach the posture, probably falling without user help.
        It basically tries and set all the motors in position as fast as possible
        """
        #self.proxy.applyPosture(posture_name, speed)
        """
        Safer, blocking call, it will chose step by step
        """
        self.proxy.goToPosture(posture_name, speed)