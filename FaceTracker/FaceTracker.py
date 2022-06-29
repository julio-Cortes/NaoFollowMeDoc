from naoqi import ALProxy

#http://doc.aldebaran.com/2-1/naoqi/trackers/alfacetracker-api.html
class FaceTracker:
    def _init_(self, ip, port):
        self.proxy = ALProxy("ALFaceTracker", ip, port)

    """
    This subscribes by default to then FaceDetect from the FaceDetection module
    Its important that the face has stiffness on 1.0 for this to work
    """
    def start_tracker(self):
        self.proxy.startTracker()

    """
    Unsubscribes to the FaceDetected event
    """
    def stop_tracker(self):
        self.proxy.stopTracker()

