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
# import random
from random import randint
from time import sleep

NORTH_GRN_TIME=randint(5, 20)
NORTH_YEL_TIME=randint(2, 5)
EAST_GRN_TIME=randint(5, 20)
EAST_YEL_TIME=randint(2, 5)
ALL_RED_TIME=rtc.getallredtime()

try:
	rtc.setup()

	while True:
		phasering1=3
		phaseflasher=0

		# normal cycle loop
		for x in range(0, 2, +1):
			if x > 0:
				# nb about to change
				phasering1=rtc.controlring1uk(phasering1)
				for ptime in range(NORTH_YEL_TIME, 0, -1):
					rtc.lcd_message("Time: " + str(ptime), "")
					sleep(1)

			# nb green
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(NORTH_GRN_TIME, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)

			# nb yellow
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(NORTH_YEL_TIME, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)
			
			# all red	
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(ALL_RED_TIME, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)

			# eb about to change 	
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(EAST_YEL_TIME, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)

			# eb green 	
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(EAST_GRN_TIME, 0, -1):
				rtc.lcd_message("Time: " + str(ptime), "")
				sleep(1)

			# eb yellow
			phasering1=rtc.controlring1uk(phasering1)
			for ptime in range(EAST_YEL_TIME, 0, -1):
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
			sleep(0.7)
		
		
except KeyboardInterrupt:
	rtc.terminate()
