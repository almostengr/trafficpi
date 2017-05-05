#!/usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: run_guess_yellow_time_double.py
# Created: 	2017-04-02
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Goal is to guess the amount of time that the traffic light will
# 		yellow for before it turns yellow. The script will provide a
# 		a random speed. Then using the yellow light formula, students
#		are to calculate the amount of time that the light will be for
#		before the light changes. Speed is given when the light turns 
#		green and countdown is started.
################################################################################

from time import sleep
import raspitraffic as rtc
import RPi.GPIO as GPIO
import lcddriver

try:
	rtc.setup()
	# display.lcd()
	display=lcddriver.lcd()
	
	rtc.debug_message("Debug mode enabled")

	phaseflasher=0
	phasering1=1
	counter=0

	while True:
		rtc.debug_message("Turning all red")

		north_grn_time=0
		north_yel_time=0
                north_speedlimit=rtc.randomspeed()
                east_speedlimit=rtc.randomspeed()
		east_grn_time=0
		east_yel_time=0
		ALL_RED_TIME=rtc.getallredtime()

		phasering1=rtc.controlring1(phasering1)

		if counter>0:
			rtc.lcd_message("Yellow Time: " + str(east_yel_time) + "s", "Game over")
			sleep(ALL_RED_TIME)

		for x in range(ALL_RED_TIME, 0, -1):	
			rtc.lcd_message("All Red Delay", "Starting in " + str(x) + "s")
			sleep(1)

		east_speedlimit=rtc.randomspeed()

		east_grn_time=rtc.calc_green_time()

		rtc.debug_message("Turning east green")

		phasering1=rtc.controlring1(phasering1)

		for x in range(east_grn_time, 0, -1):
			rtc.lcd_message("Speed Limit: " + str(east_speedlimit), "Time Remain: " + str(x) + "s")
			sleep(1)

		rtc.debug_message("Turning east yellow")

		east_yel_time=rtc.calc_yellow_time(east_speedlimit, 0)

		phasering1=rtc.controlring1(phasering1)

		rtc.lcd_message("Yellow Time: ", str(east_yel_time) + " seconds")
		
		sleep(east_yel_time)
		
		counter=1

except KeyboardInterrupt:
	rtc.log_message("Exiting")
	GPIO.cleanup()
	display.lcd_clear()
