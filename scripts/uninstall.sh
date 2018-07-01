#!/bin/bash 

#################################################################
# Description: Uninstall script to remove software installed 
# for the RapsiTraffic project.
# 
# Author: Kenny Robinson, @almostengr
# Created: 2018-07-01
#################################################################

function log_message() {
	# print message to screen
	echo $*
	
	# print message to log file	
	echo "$(date) | "$* >> /var/tmp/raspitraffc_setup.log
}

# SCRIPT MAIN
if [ $(id -u) -eq 0 ]; then
	log_message "Running script"

	log_message "Removing installed packages" 

	/usr/bin/apt-get autoremove --purge git python-dev python-rpi.gpio apache2 php7.0
	
	log_message "Done removing installed packages"
	log_message "Cleaning up"

	/usr/bin/apt-get clean

	log_message "Done cleaning up"
	log_message "Done running script"
else
	log_message "Need to be sudo or root to run script"
fi

