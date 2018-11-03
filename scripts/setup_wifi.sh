#!/bin/bash

####################################################################
# Description: Script to configure wifi settings. Script is based on
# instructions provided at
# https://pimylifeup.com/raspberry-pi-wireless-access-point/
# Author: Kenny Robinson, @almostengr
# Created: 2017-05-15
####################################################################

DATETTIME=$(date +%Y%m%d%H%M)

function log_message() {
# print message to screen and to log file
	echo $*
	echo "$(date) | "$* >> /var/tmp/raspitraffic_setup.log
}

# CHECK TO SEE IF THE SCRIPT IS BEING RAN AS ROOT
if [ $(id -u) -eq 0 ]; then
	log_message "Performing wifi Setup"

	# step 1
	apt-get update
	apt-get upgrade -y
	
	# step 2
	log_message "Installing software"
	apt-get install hostapd dnsmasq -y
	
	# step 3
	log_message "Stoping services"
	systemctl stop hostapd
	systemctl stop dnsmasq

	# step 4 and 5
	log_message "Updating dhcpcd.conf"
	touch /etc/dhcpcd.conf

	# make backup of original file
	cp -p /etc/dhcpcd.conf /etc/dhcpcd.conf.${DATETIME}

	echo "interface wlan0" >> /etc/dhcpcd.conf
	echo "static ip_address=192.168.220.1/24" >> /etc/dhcpcd.conf
	echo "nohook wpa_supplicant" >> /etc/dhcpcd.conf

	# step 6
	log_message "Restarting DHCPCD"
	systemctl restart dhcpcd 

	# step 7 and 8
	log_message "Updating hostapd.conf"
	touch /etc/hostapd/hostapd.conf

	# make backup of original file
	cp -p /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.${DATETIME}

	echo "interface=wlan0" >> /etc/hostapd/hostapd.conf
	echo "driver=nl80211" >> /etc/hostapd/hostapd.conf
	echo "hw_mode=g" >> /etc/hostapd/hostapd.conf
	echo "channel=6" >> /etc/hostapd/hostapd.conf
	echo "ieee80211n=1" >> /etc/hostapd/hostapd.conf
	echo "wmm_enabled=0" >> /etc/hostapd/hostapd.conf
	echo "macaddr_acl=0" >> /etc/hostapd/hostapd.conf
	echo "ignore_broadcast_ssid=0" >> /etc/hostapd/hostapd.conf
	echo "auth_algs=1" >> /etc/hostapd/hostapd.conf
	echo "wpa=2" >> /etc/hostapd/hostapd.conf
	echo "wpa_key_mgmt=WPA-PSK" >> /etc/hostapd/hostapd.conf
	echo "wpa_pairwise=TKIP" >> /etc/hostapd/hostapd.conf
	echo "rsn_pairwise=CCMP" >> /etc/hostapd/hostapd.conf
	echo "# This is the name of the network" >> /etc/hostapd/hostapd.conf
	echo "ssid=TrafficPi" >> /etc/hostapd/hostapd.conf
	echo "# The network passphrase" >> /etc/hostapd/hostapd.conf
	echo "wpa_passphrase=almostengr" >> /etc/hostapd/hostapd.conf

	# step 9 and 10
	cp -p /etc/default/hostapd /etc/default/hostapd.${DATETIME}
	/bin/sed 's|#DAEMON_CONF=""|DAEMON_CONF="/etc/hostapd/hostapd.conf"|g' /etc/default/hostapd.${DATETIME} > /etc/default/hostapd

	# step 11 and 12
	cp -p /etc/init.d/hostapd /etc/init.d/hostapd.${DATETIME}
	/bin/sed 's|#DAEMON_CONF=|DAEMON_CONF=/etc/hostapd/hostapd.conf|g' /etc/init.d/hostapd.${DATETIME} > /etc/init.d/hostapd

	# step 13
	mv /etc/dnsmasq.conf /etc/dnsmasq.conf.${DATETIME}

	# step 14 and 15
	touch /etc/dnsmasq.conf
	echo "interface=wlan0       # Use interface wlan0" >> /etc/dnsmasq.conf
	echo "server=1.1.1.1       # Use Cloudflare DNS" >> /etc/dnsmasq.conf
	echo "dhcp-range=192.168.220.50,192.168.220.150,12h # IP range and lease time" >> /etc/dnsmasq.conf

	# step 16 and 17
	cp -p /etc/sysctl.conf /etc/sysctl.conf.${DATETIME}
	/bin/sed 's|#net.ipv4.ip_forward=1|net.ipv4.ip_forward=1|g' /etc/sysctl.conf.${DATETIME} > /etc/sysctl.conf

	# step 18
	sh -c "echo 1 > /proc/sys/net/ipv4/ip_forward"

	# step 19
	iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE

	# step 20
	sh -c "iptables-save > /etc/iptables.ipv4.nat"

	log_message "Done performing Wifi setup"
else
	log_message "Must be root to run script."
fi
