#!/usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: run_normal_single.py
# Created: 	2017-04-03
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Runs normal operation and then flasher for traffic facing two 
# 		different directions. Phasing is based on US traffic
#		signal convention. 
################################################################################

import raspitraffic as rtc
import RPi.GPIO as GPIO
import lcddriver
import random
from time import sleep

NORTH_GRN_TIME=random.randint(5, 20)
NORTH_YEL_TIME=random.randint(2, 5)
EAST_GRN_TIME=random.randint(5, 20)
EAST_YEL_TIME=random.randint(2, 5)
ALL_RED_TIME=rtc.getallredtime()

display=lcddriver.lcd()

try:
	rtc.setup()

	while True:
		phasering1=1
		phaseflasher=0

		# normal cycle loop
		for x in range(0, 2, +1):
			phasering1=rtc.controlring1eb(phasering1)
			for ttime in range(ALL_RED_TIME, -1, -1):
				rtc.lcd_message("RED", "Time Remain: " + str(ttime) + "s")
				sleep(1)

			phasering1=rtc.controlring1eb(phasering1)
			for ttime in range(NORTH_GRN_TIME, 0, -1):
				rtc.lcd_message("GREEN", "Time Remain: " + str(ttime) + "s")
				sleep(1)

			phasering1=rtc.controlring1eb(phasering1)
			for ttime in range(NORTH_YEL_TIME, 0, -1):
				rtc.lcd_message("YELLOW", "Time Remain: " + str(ttime) + "s")
				sleep(1)

		phasering1=rtc.controlring1eb(phasering1)
		for ttime in range(ALL_RED_TIME, 0, -1):
			rtc.lcd_message("", "Time Remain: " + str(ttime) + "s")
			sleep(1)
	
		phasering1 = 0
		phaseflasher = 1

		# flasher loop
		for x in range(0, 20, +1):
			phaseflasher=rtc.controlflasher(phaseflasher)
			sleep(0.7)
		
		
except KeyboardInterrupt:
	rtc.log_message("Exiting")
	GPIO.cleanup()
	display.lcd_clear()
