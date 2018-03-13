#!/bin/bash

####################################################################
# Description: Script to configure wifi settings.
# Author: Kenny Robinson, Bit Second Tech
# Created: 2017-05-15
####################################################################  

RTNCD=255

function log_message() {
	# print message to screen
	echo $*

	# write message to log
	echo "$(date) | "$* >> /var/tmp/raspitraffic_setup.log
}

# CHECK TO SEE IF THE SCRIPT IS BEING RAN AS ROOT
if [ $(id -u) -eq 0 ]; then
	log_message "Running script"

	log_message "Performing wifi Setup"
	
	# update repositories
	apt-get update

	# installing software
	apt-get install hostapd dnsmasq -y
	
	log_message "Done performing Wifi setup"
else
	log_message "Must be root to run script."
fi
		
