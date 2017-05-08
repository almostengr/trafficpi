# /usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: run_normal_us.py
# Created: 	2017-04-03
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Runs normal operation and then flasher for a single traffic
# 		signal. Phasing is based on US traffic signal convention.
################################################################################

import raspitraffic as rtc
import random
from time import sleep

try:
	rtc.setup()
	ALL_RED_TIME=rtc.getallredtime()
	counter = 0

	while True:
		phasering1=1
		phaseflasher=0

		north_grn_time=rtc.calc_green_time()
		north_yel_time=rtc.calc_yellow_time(rtc.randomspeed(), random.randint(0, 5))
		east_grn_time=rtc.calc_green_time()
		east_yel_time=rtc.calc_yellow_time(rtc.randomspeed(), random.randint(0, 5))

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

		counter=counter+1
	
		phasering1=0
		phaseflasher=1

		if counter > 4:
			for ttime in range(30, 0, -1):
				rtc.lcd_message("Flasher Mode", "")
				phaseflasher=rtc.controlflasher(phaseflasher)
				sleep(rtc.getflashsleep())
			
			counter = 0
		
except KeyboardInterrupt:
	rtc.terminate()

