from naoqi import ALProxy


# http://doc.aldebaran.com/2-1/naoqi/audio/altexttospeech-api.html
class TextToSpeech:
    def __init__(self, ip, port):
        self.proxy = ALProxy("ALTextToSpeech", ip, port)

    """
    Normal tts, the robot will say the text sent in the params
    the language its settable, but there are not many languages installed by default
    """

    def say(self, text):
        self.proxy.say(text)
