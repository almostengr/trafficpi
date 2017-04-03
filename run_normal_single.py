#!/usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: run_normal_single.py
# Created: 	2017-04-03
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Runs normal operation and then flasher for a single traffic
# 		signal. Phasing is based on US traffic signal convention.
################################################################################

import RPi.GPIO as GPIO
import lcddriver
import sys
import random
from time import sleep

# LIST ALL OF THE PINS USED
pinOutList = [26, 19, 13, 6, 12, 16, 20, 21]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR NORTHBOUND TRAFFIC
NORTH_CR = 26
NORTH_CY = 19
NORTH_CG = 13
NORTH_LG = 20
NORTH_LY = 21
NORTH_YEL_TIME = 3
NORTH_GRN_TIME = 5

# DEBUG MODE, ENABLED=1, DISABLED=0
DEBUG=1

# SET THE VALUE OF OTHER MISC VARIABLES
if DEBUG == 1:
	ALL_RED_TIME=5
else:
	ALL_RED_TIME=10

# SET INITIAL VALUE FOR THE PHASES
phasering1 = 0
phaseflasher = 0

display=lcddriver.lcd()

def setup():
# SET UP GPIO PINS
	GPIO.setmode(GPIO.BCM)

	for i in pinOutList:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.HIGH)

	return 0

def light_on(pin):
# TURN ON THE LIGHT, HAS TO PROVIDE PIN NUMBER
	GPIO.output(pin, GPIO.LOW)
	debug_message("Pin " + str(pin) + " turned on")
	return 0

def light_off(pin):
# TURN OFF THE LIGHT, HAS TO PROVIDE PIN NUMBER
	GPIO.output(pin, GPIO.HIGH)
	debug_message("Pin " + str(pin) + " turned off")
	return 0

def debug_message(message):
# LOG ADDITIONAL MESSAGES TO THE SCREEN/LOG FILE WHEN TESTING
	if DEBUG == 1:
		log_message("DEBUG: " + message)

	return 0

def log_message(message):
# print message on LCD screen
	print message
	return 0

def lcd_message(line1, line2):
# Displays the message on the LCD screen
	display.lcd_clear()
	display.lcd_display_string(line1, 1)
	display.lcd_display_string(line2, 2)
	log_message(line1 + " | " + line2)
	return 0

def controlflasher( phase ):
# RUNS FLASHER SEQUENCE

# phase 0 - do nothing
# phase 1 - off
# phase 2 - cr
	if phase == 0:
		log_message("Do nothing")
	elif phase == 1:
		# lcd_message("EB YEL -- NB OFF", "MODE: Flasher")
		lcd_message("OFF", "Flasher Mode")
		light_off(NORTH_CR)
		# log_message("EB Yellow on")
		# log_message("NB red off")
		phase=2
	elif phase == 2:
		light_on(NORTH_CR)
		# lcd_message("EB OFF -- NB RED", "MODE: Flasher")
		lcd_message ("RED", "Flasher Mode")
		# log_message("EB yellow off")
		# log_message("NB red on")	
		phase=1
	else:
		log_message("Not valid flasher phase")
		phase=0
	return phase

def controlring1( phase ):
# RUN NORMAL RUN SEQUENCE

# phase 0 - do nothing
# phase 1 - nb cr, eb cr
# Phase 2 - nb cg, eb cr
# phase 3 - nb cy, eb cr
	debug_message("incoming phase: " + str(phase))

	if phase == 0:
		log_message("Doing nothing")
	elif phase == 1:
		light_on(NORTH_CR)
		light_off(NORTH_CY)
		light_off(NORTH_CG)
		light_off(NORTH_LG)
		light_off(NORTH_LY)

		phase = 2
		log_message("NB RED")
		# time.sleep(ALL_RED_TIME)
	elif phase == 2:
		light_off(NORTH_CR)
		light_off(NORTH_CY)
		light_on(NORTH_CG)

		phase = 3
		log_message("NB GRN")
	elif phase == 3:
		light_off(NORTH_CR)
		light_on(NORTH_CY)
		light_off(NORTH_CG)

		phase = 1
		log_message("NB YEL")
	else:
		phase = 1

	debug_message("Outgoing phase: " + str(phase))
	return phase

def controlring2():
	return 0

try:
	setup()

	while True:
		phasering1=1
		phaseflasher=0

		# normal cycle loop
		for x in range(0, 2, +1):
			phasering1=controlring1(phasering1)
			for ttime in range(ALL_RED_TIME, 0, -1):
				lcd_message("RED", "Time Remain: " + str(ttime) + "s")
				sleep(1)

			phasering1=controlring1(phasering1)
			# sleep(NORTH_GRN_TIME)
			for ttime in range(NORTH_GRN_TIME, 0, -1):
				lcd_message("GREEN", "Time Remain: " + str(ttime) + "s")
				sleep(1)

			phasering1=controlring1(phasering1)
			# sleep(ALL_RED_TIME)
			for ttime in range(NORTH_YEL_TIME, 0, -1):
				lcd_message("YELLOW", "Time Remain: " + str(ttime) + "s")
				sleep(1)

		phasering1=controlring1(phasering1)
		for ttime in range(ALL_RED_TIME, 0, -1):
			lcd_message("RED", "Time Remain: " + str(ttime) + "s")
			sleep(1)
	
		phasering1 = 0
		phaseflasher = 1

		# flasher loop
		for x in range(0, 20, +1):
			phaseflasher=controlflasher(phaseflasher)
			sleep(0.7)
		
		
except KeyboardInterrupt:
	log_message("Exiting")
	GPIO.cleanup()
	display.lcd_clear()
