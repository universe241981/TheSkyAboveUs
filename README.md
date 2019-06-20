# TheSkyAboveUs
An all sky imaging system that use Raspberry Pi(all type of RPi mainboard) and Pi camera

Due to the exposure time limitation of the Pi camera v1.3 at maximum 6 seconds, such system only usable at area with relatively light polluted sky.

# Switch between AP mode and WIFI mode
From AP mode to WIFI mode:
---------------------------
<sudo systemctl stop hostapd>

sudo nano /etc/dhcpcd.conf

Inside dhcpcd.conf, remove/comment out the lines related to the static IP address (in my case, the last two lines in the file):

#static ip_address=192.168.10.1/24

#static routers=192.168.10.1

Edit the wpa_supplicant to enable WIFI connection:

sudo nano /etc/wpa_supplicant/wpa_supplicant.conf

sudo reboot
