#!/usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: guess_yellow_time.py
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
import RPi.GPIO as GPIO
import lcddriver
import raspitraffic as rtc

display=lcddriver.lcd()

try:
	# CODE TO RUN GOES HERE

	rtc.setup()
	rtc.lamptest()

except KeyboardInterrupt:
	rtc.log_message("Exiting")
	GPIO.cleanup()
	display.lcd_clear()
