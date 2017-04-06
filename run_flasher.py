#!/usr/bin/python

################################################################################
# Project:      Traffic Control
# Script Usage: run_flasher.py
# Created:      2017-04-02
# Author:       Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:  Flash lights as if a malfunction or power outage has occurred.
################################################################################

from raspitraffic import controlflasher
from raspitraffic import log_message
from raspitraffic import setup
from time import sleep
import lcddriver
import RPi.GPIO as GPIO

try:
	display=lcddriver.lcd()
	
	setup()

	# CODE TO RUN GOES HERE
	phaseflasher=1

	while True:
		phaseflasher=controlflasher(phaseflasher)
		sleep(.5)
except KeyboardInterrupt:
	log_message("Exiting")
	GPIO.cleanup()
	display.lcd_clear()
