from picamera import PiCamera
import time
from time import sleep
camera = PiCamera()
while True:
    DATE = (time.strftime("%y%m%d_%H:%M:%S"))
    variable = "/home/aspi/AllSkyData/" + DATE + ".jpg"
    camera.capture(variable)
    sleep(5)
