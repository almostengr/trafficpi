#!/bin/bash

####################################################################
# Script to test 

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
	
	# update repositories
	apt-get update

	# installing software
	apt-get install hostadp dnsmasq -y
else
	log_message "Must be root to run script."
fi
		
	
main $*
