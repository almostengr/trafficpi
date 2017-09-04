# /usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: run_normal_single.py
# Created: 	2017-04-03
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Runs normal operation and then flasher for a single traffic
# 		signal. Phasing is based on US traffic signal convention.
################################################################################

import raspitraffic as rtc
import lcddriver
import random
from time import sleep

display=lcddriver.lcd()

try:
	rtc.setup()

	north_grn_time=rtc.calc_green_time()
	north_yel_time=rtc.calc_yellow_time(rtc.randomspeed(), random.randint(0, 5))
	east_grn_time=rtc.calc_green_time()
	east_yel_time=rtc.calc_yellow_time(rtc.randomspeed(), random.randint(0, 5))
	ALL_RED_TIME=rtc.getallredtime()

	while True:
		phasering1=1
		phaseflasher=0

		# normal cycle loop
		for x in range(0, 2, +1):
			phasering1=rtc.controlring1(phasering1)
			for ttime in range(ALL_RED_TIME, 0, -1):
				rtc.lcd_message("Time Remain: ", str(ttime) + "s")
				sleep(1)

			phasering1=rtc.controlring1(phasering1)
			for ttime in range(north_grn_time, 0, -1):
				rtc.lcd_message("Time Remain: ", str(ttime) + "s")
				sleep(1)

			phasering1=rtc.controlring1(phasering1)
			for ttime in range(int(round(north_yel_time, 0)), 0, -1):
				rtc.lcd_message("Time Remain: ", str(ttime) + "s")
				sleep(1)
	
			phasering1=rtc.controlring1(phasering1)
			for ttime in range(ALL_RED_TIME, 0, -1):
				rtc.lcd_message("Time Remain: ", str(ttime) + "s")
				sleep(1)

			phasering1=rtc.controlring1(phasering1)
			for ttime in range(east_grn_time, 0, -1):
				rtc.lcd_message("Time Remain: ", str(ttime) + "s")
				sleep(1)

			phasering1=rtc.controlring1(phasering1)
			for ttime in range(int(round(east_yel_time, 0)), 0, -1):
				rtc.lcd_message("Time Remain: ", str(ttime) + "s")
				sleep(1)

		phasering1=rtc.controlring1(phasering1)
		for ttime in range(ALL_RED_TIME, 0, -1):
			rtc.lcd_message("Time Remain: ", str(ttime) + "s")
			sleep(1)
	
		phasering1 = 0
		phaseflasher = 1

		# flasher loop
		for x in range(0, 20, +1):
			phaseflasher=rtc.controlflasher(phaseflasher)
			sleep(rtc.getflashsleep())
		
		
except KeyboardInterrupt:
	rtc.terminate()

