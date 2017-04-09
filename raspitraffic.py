#!/usr/bin/python

################################################################################
# Project: 	Raspi Traffic Control
# Script Usage: raspitraffic.py
# Created: 	2017-04-02
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Core script which all the functions for controlling the lights
# 		are contained. 
################################################################################

from time import sleep
import RPi.GPIO as GPIO
import lcddriver
import random

# DEBUG MODE, ENABLED=1, DISABLED=0
DEBUG=0

# LIST ALL OF THE PINS USED
pinOutList = [37, 35, 33, 31, 29, 23, 21, 19]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR NORTHBOUND TRAFFIC
NORTH_CR = 37
NORTH_CY = 35
NORTH_CG = 33
NORTH_LG = 31
NORTH_LY = 29

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR THE EASTBOUND TRAFFIC
EAST_CR = 23
EAST_CY = 21
EAST_CG = 19

display=lcddriver.lcd()
ALL_RED_TIME=5

def setup():
# SET UP GPIO PINS
	GPIO.setmode(GPIO.BOARD)

	for i in pinOutList:
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.HIGH)

	return 0

def getallredtime():
# GETS THE VALUE OF THE ALL RED TIME
	return ALL_RED_TIME

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
# Displays the message on the LCD screen and computer screen
	display.lcd_clear()
	display.lcd_display_string(line1, 1)
	display.lcd_display_string(line2, 2)
	log_message(line1 + " | " + line2)
	return 0

def terminate():
# WHEN COMMAND TO EXIT IS GIVEN, THEN RESET EVERYTHING BACK TO DEFAULT
	log_message("Exiting")
        GPIO.cleanup()
        display.lcd_clear()

def controlflasher( phase ):
# runs flasher SEQUENCE
	if phase == 0:
		log_message("Do nothing")
	elif phase == 1:
		lcd_message("Flasher Mode", "EB YEL, NB OFF")
		light_off(NORTH_CG)
		light_off(NORTH_CY)
		light_off(NORTH_LG)
		light_off(NORTH_LY)
		light_off(NORTH_CR)
		light_off(EAST_CR)
		light_on(EAST_CY)
		light_off(EAST_CG)
		phase=2
	elif phase == 2:
		light_on(NORTH_CR)
		light_off(EAST_CY)
		lcd_message ("Flasher Mode", "EB OFF, NB RED")
		phase=1
	else:
		log_message("Not valid flasher phase")
		phase=0
	return phase

def calc_yellow_time( speed, grade ):
# CALCULATE THE AMOUNT OF YELLOW LIGHT TIME
	# y = 1 + ((1.47 * speed) / (2 * (10 * (grade / 100) * 32.2))
	yel_time = 1 + ((1.47 * speed) / (2 * (10 + (0 / 100) * 32.2)))
	log_message("Yellow Time: " + str(yel_time))
	return yel_time

def calc_green_time():
# SET A RANDOM VALUE FOR THE GREEN TIME
	grn_time=random.randint(15, 35)

	log_message("Green Time: " + str(grn_time))
	return grn_time

def controlring1( phase ):
# RUN NORMAL RUN SEQUENCE

# phase 0 - do nothing
# phase 1 - nb cr, eb cr
# Phase 2 - nb cg, eb cr
# phase 3 - nb cy, eb cr
# phase 4 - nb cr, eb cr
# phase 5 - nb cr, eb cg
# phase 6 - nb cr, eb cy
	debug_message("incoming phase: " + str(phase))

	if phase == 0:
		log_message("Doing nothing")
	elif phase == 1:
		log_message("NB RED -- EB RED")
		light_on(NORTH_CR)
		light_off(NORTH_CY)
		light_off(NORTH_CG)
		light_off(NORTH_LG)
		light_off(NORTH_LY)
		light_on(EAST_CR)
		light_off(EAST_CY)
		light_off(EAST_CG)

		phase = 2
	elif phase == 2:
		log_message("NB GRN -- EB RED")
		light_off(NORTH_CR)
		light_off(NORTH_CY)
		light_on(NORTH_CG)
		light_on(EAST_CR)
		light_off(EAST_CY)
		light_off(EAST_CG)

		phase = 3
	elif phase == 3:
		light_off(NORTH_CR)
		light_on(NORTH_CY)
		light_off(NORTH_CG)
		light_on(EAST_CR)
		light_off(EAST_CY)
		light_off(EAST_CG)

		phase = 4 
		log_message("NB YEL -- EB RED")
	elif phase == 4:
		light_on(NORTH_CR)
		light_off(NORTH_CY)
		light_off(NORTH_CG)
		light_on(EAST_CR)
		light_off(EAST_CY)
		light_off(EAST_CG)
		
		phase = 5
		log_message("NB RED -- EB RED")
	elif phase == 5:
		light_on(NORTH_CR)
		light_off(NORTH_CY)
		light_off(NORTH_CG)
		light_off(EAST_CR)
		light_off(EAST_CY)
		light_on(EAST_CG)
		
		phase = 6 
		log_message("NB RED -- EB GRN")
	elif phase == 6:
		light_on(NORTH_CR)
		light_off(NORTH_CY)
		light_off(NORTH_CG)
		light_off(EAST_CR)
		light_on(EAST_CY)
		light_off(EAST_CG)

		phase = 1 
		log_message("NB RED -- EB YEL")
	else:
		phase = 1

	debug_message("Outgoing phase: " + str(phase))
	return phase

def randomspeed():
	speed=random.randint(25,50)
	return speed

def allon():
# TURNS ON ALL OF THE LIGHTS
	lcd_message("ALL LIGHTS ON", "")
	for i in pinOutList:
		light_on(i)
	sleep(3)

def alloff():
# TURNS OFF ALL OF THE LIGHTS
	lcd_message("ALL LIGHTS OFF", "")
	for i in pinOutList:
		light_off(i)
	sleep(3)

def lamptest():
	lcd_message("LAMP TEST", "")

	for i in pinOutList:
		light_on(i)
		lcd_message("LAMP TEST", "Pin " + str(i) + " on")
		sleep(1)

	lcd_message("LAMP TEST", "ALL ON")
	sleep(10)

	for i in pinOutList:
		light_off(i)
		lcd_message("LAMP TEST", "Pin " + str(i) + " off")
		sleep(1)

	lcd_message("LAMP TEST", "ALL OFF")
	sleep(3)
	sleep(3)	
	display.lcd_clear()

