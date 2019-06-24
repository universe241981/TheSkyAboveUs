#For Installation of Picamera for enable python control of Pi camera 
#https://picamera.readthedocs.io/en/release-1.13/install.html

from picamera import PiCamera
import time
from time import sleep
camera = PiCamera()
camera.resolution = (2592, 1944)
sleep(2)
DATE = (time.strftime("%y%m%d_%H%M%S"))
variable = "/home/aspi/AllSkyData/" + DATE + ".jpg"
camera.capture(variable)


from time import sleep
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
camera.start_preview()
wait()
for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    wait()
