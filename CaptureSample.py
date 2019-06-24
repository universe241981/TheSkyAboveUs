#For Installation of Picamera for enable python control of Pi camera 
#https://picamera.readthedocs.io/en/release-1.13/install.html

from picamera import PiCamera
import time
from time import sleep
camera = PiCamera()
while True:
    DATE = (time.strftime("%y%m%d_%H:%M:%S"))
    variable = "/home/aspi/AllSkyData/" + DATE + ".jpg"
    camera.capture(variable)
    sleep(5)
