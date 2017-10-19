#!/bin/bash 

#################################################################
# Description: Setup the required software to run the scripts.
# 
# Author: Kenny Robinson, Bit Second Tech
# Created: 2017-05-15
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

	log_message "Updating software packages"

	/usr/bin/apt-get update
	
	log_message "Done updating software packages"
	
	log_message "Upgrading software packages"

	/usr/bin/apt-get upgrade -y 

	log_message "Done upgrading software packages"

	log_message "Installing needed packages" 

	/usr/bin/apt-get python git
	
	log_message "Done installing needed packages"
	
	log_message "Displaying python version"

	/usr/bin/python --version
	
	log_message "Done displaying python version"

	log_message "Running LCD install script"

	# run LCD install script
	. $(pwd)/lcd/install.sh

	log_message "Done running LCD install script"
else
	log_message "Need to be sudo or root to run script"
fi

