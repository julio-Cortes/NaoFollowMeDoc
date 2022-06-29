from naoqi import ALProxy


# http://doc.aldebaran.com/2-1/naoqi/peopleperception/alfacedetection.html#alfacedetection
class FaceDetection:
    def __init__(self, ip, port):
        self.proxy = ALProxy("ALFaceDetection", ip, port)
        """
        this subscribes to the proxy, making the module write in memory with a 500 second period
        """
        self.proxy.subscribe("Test_Face", 500, 0.0)

    """
    Enabled by default, the rest of the face detection features will run faster with this off
    """
    def enable_recognition(self):
        self.proxy.enableRecognition(True)

    """
    Disables face recognition
    """
    def disable_recognition(self):
        self.proxy.enableRecognition(False)


    """
    Receives the name of the face to learn, it returns true if it was learned, false if the operation
    failed.
    It needs better conditions that face detection (light and distance)
    """
    def learn_face(self, face_name):
        return self.proxy.learnFace(face_name)

    """
    Same as learn face but it allows to improve the recognition of the name passed on
    :return values are the same.
    """
    def re_learn_face(self, face_name):
        return self.proxy.reLearnFace(face_name)

    """
    Deletes all learned faces from the database
    """
    def clear_database(self):
        self.proxy.clearDatabase()


ip = "pop-os.local"
port = 9559
# Small program to learn a face
if __name__ == "__main__":
    face_detection = FaceDetection(ip, port)
    print (face_detection.learn_face("FaceName"))
