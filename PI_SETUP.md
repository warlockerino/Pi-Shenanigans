# Pi-Shenanigans


Basic Raspberry Setup Cheatsheet:
-------- BURN ISO ---------------------------------------------------
lsblk

dd bs=1M if=****.img of=/dev/***

sudo sync


-------- Enable WIFI ------------------------------------------------
// unsupported Dongle

sudo nano /etc/network/interfaces

auto lo

iface lo inet loopback
iface eth0 inet dhcpallow-hotplug wlan0
iface wlan0 inet dhcp
wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
iface default inet dhcp

// Scan available WiFis
sudo iwlist wlan0 scan


//Edit WiFi connections
sudo nano /etc/wpa_supplicant/wpa_supplicant.conf // network ={ssid="name" psk="pass"}

-------- CREATE .LOCAL ----------------------------------------------

DEP.: avahi-daemon

sudo nano /etc/hosts // 127.0.1.1 <name>

sudo nano /etc/hostname  //  <name>

sudo /etc/init.d/hostname.sh

---------- CHANGE KEYBOARD LAYOUT------------------------------------

sudo nano /etc/default/keyboard
