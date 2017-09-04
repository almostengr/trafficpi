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

		# nb grn, eb red
		phasering1=rtc.controlring1(phasering1)
		for ttime in range(north_grn_time, 0, -1):
			rtc.lcd_message("NB GRN, EB RED", "Time Remain: " + str(ttime) + "s")
			sleep(1)
	
		# nb yel, eb red
		phasering1=rtc.controlring1(phasering1)
		for ttime in range(int(round(north_yel_time, 0)), 0, -1):
			rtc.lcd_message("NB YEL, EB RED", "Time Remain: " + str(ttime) + "s")
			sleep(1)
		
		# all red phase
		phasering1=rtc.controlring1(phasering1)
		for ttime in range(ALL_RED_TIME, 0, -1):
			rtc.lcd_message("NB RED, EB RED", "Time Remain: " + str(ttime) + "s")
			sleep(1)

		# nb red, eb grn
		phasering1=rtc.controlring1(phasering1)
		for ttime in range(east_grn_time, 0, -1):
			rtc.lcd_message("NB RED, EB GRN", "Time Remain: " + str(ttime) + "s")
			sleep(1)

		# nb red, eb yel
		phasering1=rtc.controlring1(phasering1)
		for ttime in range(int(round(east_yel_time, 0)), 0, -1):
			rtc.lcd_message("NB RED, EB YEL", "Time Remain: " + str(ttime) + "s")
			sleep(1)
	
		# all red
		phasering1=rtc.controlring1(phasering1)
		for ttime in range(ALL_RED_TIME, 0, -1):
			rtc.lcd_message("NB RED, EB RED", "Time Remain: " + str(ttime) + "s")
			sleep(1)

except KeyboardInterrupt:
	rtc.terminate()

