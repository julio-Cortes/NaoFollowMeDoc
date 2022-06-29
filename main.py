from naoqi import ALProxy
import time
from FaceDetection.FaceDetection import FaceDetection
from FaceTracker.FaceTracker import FaceTracker
from Memory.Memory import Memory
from Motion.Motion import Motion
from Posture.Posture import Posture
from TextToSpeech.TextToSpeech import TextToSpeech

"""
This program as it is, will make the robot detect faces, and move towards them, if the nao recognizes the face, it will
call his by the name it has stored, this will be done under 2 seconds cycle to not overload the OS of the robot.
"""



ip = "pop-os.local"
port = 9559

"""
The robot version of print hello world, it's used to test if the robot connection went right and 
the get of the proxy's are working
"""
tts = TextToSpeech(ip, port)
tts.say("I see the duck")

# The subscribe method for face detection might be unnecessary, since face_tracker should do that on its own.
# Although the access to the face information its being done from the detection along with the memory module
face_detection = FaceDetection(ip, port)
face_tracker = FaceTracker(ip, port)
posture = Posture(ip, port)
# posture.set_posture("Crouch")
face_detection.enable_recognition()
face_tracker.start_tracker()
# face_detection.learn_face("Put here the face name")

"""
this code is missing the angle correction
"""
if __name__ == "__main__":
    finished = False
    while not finished:
        motion = Motion(ip, port)
        memory = Memory(ip, port)
        time.sleep(2)
        val = memory.get_data("FaceDetected")
        # Face deteceted
        if (val and isinstance(val, list) and len(val) >= 2):
            tts.say("I see a human")
            face_info_array = val[1]
            try:
                for j in range(len(face_info_array) - 1):
                    faceInfo = face_info_array[j]

                    # First Field = Shape info.
                    faceShapeInfo = faceInfo[0]

                    # Second Field = Extra info (empty for now).
                    faceExtraInfo = faceInfo[1]
                    print "FACE " + str(j)
                    if (len(faceExtraInfo) >= 3):
                        # The 3rd element in the array it's the face name
                        tts.say("Hello" + str(faceExtraInfo[2]))
                        print "recognized face:" + str(faceExtraInfo[2])

                    motion.walk(0.5, 0, motion.get_head_angle())
                    """
                    if this its enabled you can make the robot stop after a certain distance from the human is reached
                    otherwise its an infinite loop
                    """
                    # if faceShapeInfo[3] >= 0.15:
                    #   finished = True
            except Exception, e:
                print "faces detected, but it seems getData is invalid. ALValue ="
                print val
                print "Error msg %s" % (str(e))

        else:
            tts.say("I dont see a human")
            print "No face detected"

    face_tracker.stop_tracker()

