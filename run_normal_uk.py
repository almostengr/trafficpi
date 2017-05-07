#!/usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: run_normal_uk.py
# Created: 	2017-04-09
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Runs normal operation and then flasher for a single traffic
# 		signal. Phasing is based on UK traffic signal convention.
################################################################################

import raspitraffic as rtc
from random import randint
from time import sleep

ALL_RED_TIME=rtc.getallredtime()

try:
	rtc.setup()

	while True:
		phasering1=2
		phaseflasher=0

		north_grn_time=randint(5, 15)
		north_yel_time=randint(2, 5)
		east_grn_time=randint(5, 15)
		east_yel_time=randint(2, 5)

		# normal cycle loop
		for x in range(0, 2, +1):

			# nb green
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(north_grn_time, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)

			# nb yellow
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(north_yel_time, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)
			
			# all red	
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(ALL_RED_TIME, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)

			# eb green 	
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(east_grn_time, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)

			# eb yellow
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(east_yel_time, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)

			# all red	
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(ALL_RED_TIME, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)

		phasering1 = 0
		phaseflasher = 1

		# flasher loop
		for x in range(0, 20, +1):
			phaseflasher=rtc.controlflasher(phaseflasher)
			sleep(rtc.getflashsleep())
		
		
except KeyboardInterrupt:
	rtc.terminate()
