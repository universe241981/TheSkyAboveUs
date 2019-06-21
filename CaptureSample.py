from picamera import PiCamera
import time
from time import sleep
camera = PiCamera()
while True:
    fname = (time.strftime("%y%b%d_%H:%M:%S"))
    variable = "/home/pi/Documents/ZeroWGarden/Pics/" + fname + ".jpg"
    camera.capture(variable)
    sleep(5)
