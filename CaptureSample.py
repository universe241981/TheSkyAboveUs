#For Installation of Picamera for enable python control of Pi camera 
#https://picamera.readthedocs.io/en/release-1.13/install.html
# $ sudo apt-get update
# $ sudo apt-get install python-picamera python3-picamera

from picamera import PiCamera
import time
from time import sleep
camera = PiCamera()
camera.resolution = (2592, 1944)
sleep(2)
DATE = (time.strftime("%Y%m%d_%H%M%S"))
variable = "/home/aspi/AllSkyData/" + DATE + ".jpg"
camera.capture(variable)

---------------------------------------------------

import picamera
import time

while True:
    with picamera.PiCamera() as camera:
        camera.resolution = camera.MAX_RESOLUTION
        time.sleep(2) # Camera warm-up time
        DATE = (time.strftime("%Y%m%d_%H%M%S"))
        camera.capture("/home/aspi/AllSkyData/" + DATE + ".jpg")
    # Capture one image a minute
    time.sleep(60)

----------------------------------------------------  

#Kenny's Pi code
from picamera import PiCamera
from fractions import Fraction
import datetime
from time import strftime
import datetime, time
from time import strftime

date_time = ''
date_time = strftime('%Y', time.localtime())
date_time = date_time + strftime('%m', time.localtime())
date_time = date_time + strftime('%d_', time.localtime())
date_time = date_time + strftime('%H:%M:%S', time.localtime())
camera = PiCamera(resolution=(2592, 1944))
camera.sensor_mode = 2
camera.exposure_mode = 'auto'  # off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake and fireworks
camera.awb_mode = 'auto'   # off, auto, sunlight, cloudy, shade, tungsten, fluorescent, incandescent, flash, and horizon
camera.shutter_speed = 0
camera.iso = 0
camera.brightness = 80  # 0 to 100
camera.contrast = 80  # 0 to 100
camera.start_preview()
time.sleep(60)
camera.capture(date_time +'.jpg')
camera.stop_preview()

--------------------------------------------------

from time import sleep
from picamera import PiCamera
from datetime import datetime

camera = PiCamera()
camera.resolution = (2592, 1944)

for filename in camera.capture_continuous('{timestamp:%Y%m%d-%H%M%S}.jpg'):
    camera.capture_continuous('/home/aspi/AllSkyData/{timestamp:%Y%m%d-%H%M%S}.jpg')
    sleep(30)
    
--------------------------------------------------

from picamera import PiCamera
import time
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)

while True:
    DATE = (time.strftime("%Y%m%d_%H%M%S"))
    camera.capture("/home/aspi/AllSkyData/" + DATE + ".jpg")
    sleep(30)

    # 640×480, 800×600, 960×720, 1024×768, 1280×960, 1400×1050, 1440×1080, 1600×1200, 1856×1392, 1920×1440, and 2048×1536
