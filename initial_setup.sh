#!/bin/bash

####################################################
# Script Usage: initial_setup.sh
# 
# Author: Kenny Robinson, Almost Engineer; @almostengr
# 
# Description: Script installs the required files and software
# packages to run as a functioning traffic light.
####################################################

# MAKE SURE THAT THE ROOT USER IS RUNNING THE SCRIPT.
if [ "$(id -u)" == "0" ]; then
	/bin/date

	echo "Updating repositories"

	/usr/bin/apt-get update

	echo "Installing and updating packages"
	
	/usr/bin/apt-get install -y git openssh-server python-pip

	echo "Running LCD install script"

	# run LCD install script
	. $(pwd)/lcd/install.sh

	echo "Installation completed"

	/bin/date
else
	# THROW ERROR IF NOT RUNNING AS ROOT
	/bin/echo "ERROR: Must be running as root to run script"
fi

