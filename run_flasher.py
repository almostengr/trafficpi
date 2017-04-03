#!/usr/bin/python

################################################################################
# Project: 	Traffic Control
# Script Usage: guess_yellow_time.py
# Created: 	2017-04-02
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Flash lights as if malfunction has occurred.
################################################################################

import time
import RPi.GPIO as GPIO
import lcddriver
import sys
import random

# LIST ALL OF THE PINS USED
pinOutList = [26, 19, 13, 6, 12, 16, 20, 21]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR NORTHBOUND TRAFFIC
NORTH_CR = 26
NORTH_CY = 19
NORTH_CG = 13
NORTH_LG = 20
NORTH_LY = 21
NORTH_SPEEDLIMIT = 45
NORTH_YEL_TIME = 0
NORTH_GRN_TIME = 0

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR THE EASTBOUND TRAFFIC
EAST_CR = 6
EAST_CY = 12
EAST_CG = 16
EAST_SPEEDLIMIT = 25
EAST_YEL_TIME = 0
EAST_GRN_TIME = 0

# DEBUG MODE, ENABLED=1, DISABLED=0
DEBUG=0

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
# runs flasher SEQUENCE
	if phase == 0:
		log_message("Do nothing")
	elif phase == 1:
		# lcd_message("EB YEL -- NB OFF", "MODE: Flasher")
		lcd_message("EB YEL", "NB OFF")
		light_on(EAST_CY)
		light_off(NORTH_CR)
		phase=2
	elif phase == 2:
		light_on(NORTH_CR)
		light_off(EAST_CY)
		lcd_message ("EB OFF", "NB RED")
		phase=1
	else:
		log_message("Not valid flasher phase")
		phase=0
	return phase

try:
	setup()
	phaseflasher=1

	while True:
		phaseflasher=controlflasher( phaseflasher )
		time.sleep(0.5)

except KeyboardInterrupt:
	log_message("Exiting")
	GPIO.cleanup()
	display.lcd_clear()
