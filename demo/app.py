from flask import Flask, render_template, Response, jsonify, request
from camera import VideoCamera
import cv2
import requests
import json

DEMO_BOARD_IP = "192.168.68.150"
DEMO_BOARD_PORT = "5002"

app = Flask(__name__)

video_stream1 = VideoCamera()
#video_stream2 = VideoCamera("http://192.168.68.102:8080/video")

@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
     return Response(gen(video_stream1),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port="5001")


