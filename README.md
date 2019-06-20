# TheSkyAboveUs
An all sky imaging system that use Raspberry Pi(all type of RPi mainboard) and Pi camera

Due to the exposure time limitation of the Pi camera v1.3 at maximum 6 seconds, such system only usable at area with relatively light polluted sky.

[NOTE] 2019-06-20
-
If use Pi0W and connected to home network, the PHP can be view as normal without any problem.
But if Remot3it was setup and view the PHP page via remot3it, Pi0W will halt from operation.
This only happen on Pi0W. Other RPi board got no issue at all.

# Switch between AP mode and WIFI mode
From AP mode to WIFI mode:
-
    sudo nano /etc/dhcpcd.conf
 
Inside dhcpcd.conf, remove/comment out the lines related to the static IP address (in my case, the last two lines in the file):

#static ip_address=192.168.10.1/24

#static routers=192.168.10.1

Edit the wpa_supplicant.conf to enable WIFI connection:
-
     sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
    
Edit:

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country="country code"

    network={
    
        ssid="xxxx"
        psk="xxxx"
        id_str="xxxx"
    }

Then reboot,

    sudo reboot

From WIFI mode to AP mode:
-
    sudo nano /etc/dhcpcd.conf
 
At the bottom of the file, edit:

    interface wlan0
        static ip_address=192.168.10.1/24
        static routers=192.168.10.1

Then,

    sudo systemctl unmask hostapd
    sudo systemctl enable hostapd

Then reboot,
    
    sudo reboot
