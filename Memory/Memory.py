from naoqi import ALProxy

#http://doc.aldebaran.com/2-1/naoqi/core/almemory-api.html#ALMemoryProxy::getData__ssCR
class Memory:
    def __init__(self, ip, port):
        self.proxy = ALProxy("ALMemory", ip, port)

    """
    Gets the file with the filename received from the memory available by the proxy
    :returns a list of objects for the "FaceDetected" case
    """
    def get_data(self, filename):
        return self.proxy.getData(filename)
