import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (640, 480)
    camera.start_preview()
    camera.start_recording('/home/pi/video.h264')
    camera.stop_recording()
    camera.stop_preview()
