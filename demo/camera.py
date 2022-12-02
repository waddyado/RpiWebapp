import cv2

class VideoCamera(object):
    def __init__(self, source = 0):
        self.video = cv2.VideoCapture(source)

    def __del__(self):
        self.video.release()        

    def get_frame(self):
        ret, frame = self.video.read()

        # Here is where we can put things like overlays or cropping
        #frame = frame[200:-50, 100:-100, :]

        ret, jpeg = cv2.imencode('.jpg', frame)

        return jpeg.tobytes()
