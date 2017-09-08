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
import sys
import os

# DEBUGGING MODE, DISABLED=0, ENABLED=1
DEBUG=0

# LIST ALL OF THE PINS USED
pinOutList = [37, 35, 33, 31, 29, 23, 21, 19]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR NORTHBOUND TRAFFIC
# NORTH_CR = 37
# NORTH_CY = 35
# NORTH_CG = 33
# NORTH_LG = 31
# NORTH_LY = 29

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR THE EASTBOUND TRAFFIC
EAST_CR = 23
EAST_CY = 21
EAST_CG = 19

# DEFINE CONSTANTS
LMPON=GPIO.LOW
LMPOFF=GPIO.HIGH
ALL_RED_TIME=2
FLASHER_DELAY=.7

display=lcddriver.lcd()

def setup():
# SET UP GPIO PINS
	GPIO.setmode(GPIO.BOARD)
	
	# loop through each of the pins and define it.
	# tun on all the lights once setup
	
	# log_message("Performing setup")
	lcd_message("Performing setup", "Please wait...")
	
	for i in pinOutList:
		debug_message("Setting up and activiating pin " + str(i))
		GPIO.setup(i, GPIO.OUT)
		GPIO.output(i, GPIO.LOW)

	debug_message("Waiting")

	sleep(2)

	# turn off all the lights
	for i in pinOutList:
		GPIO.output(i, GPIO.HIGH)

	# log_message("Done performing setup")
	lcd_message("Done performing setup", "")
		
	return 0

def flashsleep():
# SLEEPS FOR THE DEFINED DELAY
	sleep(FLASHER_DELAY)

def getflashsleep():
# GETS THE SLEEP VALUE FOR THE FLASHER FUNCTION
	return FLASHER_DELAY
	
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
# print message on computer screen
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

def controlflasher(phase):
# runs flasher sequence

	if phase == 0:
		log_message("Do nothing")
	
	# flash nb yellow, eb red
	elif phase == 1:
		nblight(LMPOFF, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPOFF)
		# lcd_message("Flasher Mode", "EB OFF, NB YEL")
		phase=2
	elif phase == 2:
		nblight(LMPOFF, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		# lcd_message ("Flasher Mode", "EB RED, NB OFF")
		phase=1

	# flash red lights
	elif phase == 3:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPOFF)
		phase=4
	elif phase == 4:
		nblight(LMPOFF, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase=3

	# flash yellow lights
	elif phase == 5:
		nblight(LMPOFF, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPOFF)
		phase = 6
	elif phase == 6:
		nblight(LMPOFF, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPON, LMPOFF)
		phase = 5

	# flash green lights
	elif phase == 7:
		nblight(LMPOFF, LMPOFF, LMPON, LMPOFF, LMPON)
		eblight(LMPOFF, LMPOFF, LMPOFF)
		phase = 8
	elif phase == 8:
		nblight(LMPOFF, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPON)
		phase = 7

	# flash with nb red, eb yellow
	elif phase == 9:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPOFF)
		phase = 10
	elif phase == 10:
		nblight(LMPOFF, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPON, LMPOFF)
		phase = 9

	else:	
		log_message("Not valid flasher phase")
		phase = 0
	return phase


def calc_yellow_time( speed, grade ):
# CALCULATE THE AMOUNT OF YELLOW LIGHT TIME
	# y = 1 + ((1.47 * speed) / (2 * (10 * (grade / 100) * 32.2))
	yel_time = 1 + ((1.47 * speed) / (2 * (10 + (0 / 100) * 32.2)))
	# yel_time = 1 +  644
	log_message("Yellow Time: " + str(yel_time))
	return yel_time

def calc_green_time():
# SET A RANDOM VALUE FOR THE GREEN TIME
	grn_time=random.randint(10, 45)
	log_message("Green Time: " + str(grn_time))
	return grn_time

def nblight(cirred, ciryel, cirgrn, lefyel, lefgrn):
# CONTROLS THE LAMPS ON THE NORTHBOUND LIGHT. DESIGNED TO INCLUDE LEFT TURN
	GPIO.output(NORTH_CR, cirred)
	GPIO.output(NORTH_CY, ciryel)
	GPIO.output(NORTH_CG, cirgrn)
	GPIO.output(NORTH_LY, lefyel)
	GPIO.output(NORTH_LG, lefgrn)

def eblight(cirred, ciryel, cirgrn):
# CONTROLS THE LAMPS ON THE EASTBOUND LIGHT. DOESNT HAVE LEFT TURN
	GPIO.output(EAST_CR, cirred)
	GPIO.output(EAST_CY, ciryel)
	GPIO.output(EAST_CG, cirgrn)

def controlring1uk(phase):
# RUN NORMAL SEQUENCE WITH UK PHASING

# phase 0 - do nothing
# phase 1 - nb cr cy, eb cr
# phase 2 - nb cg, eb cr
# phase 3 - nb cy, eb cr
# phase 4 - nb cr, eb cr cy
# phase 5 - nb cr, eb cg
# phase 6 - nb cr, eb cy
	
	debug_message("incoming phase: " + str(phase))
	
	if phase == 0:
		log_message("Do nothing")
	elif phase == 1:
		nblight(LMPON, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 2
	elif phase == 2:
		nblight(LMPOFF, LMPOFF, LMPON, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase=3
	elif phase == 3:
		nblight(LMPOFF, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 4
	elif phase == 4:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPON, LMPOFF)
		phase = 5
	elif phase == 5:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPON)
		phase = 6
	elif phase == 6:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPON, LMPOFF)
		phase = 1 
	else:
		phase=1
	
	debug_message("outgoing phase " + str(phase))
	return phase

def controlredlightgreenlight(phase):
# SEQUENCE FOR RED LIGHT GREEN LIGHT GAME. PLAYED WITH ONLY ONE TRAFFIC LIGHT.

# phase 0 - do nothing
# phase 1 - red light
# phase 2 - green light
	if phase == 0:
		log_message("Doing nothing")
	elif phase == 1:
		nblight(LMPOFF, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		lcd_message("Red Light!", "")
		phase = 2
	elif phase == 2:
		nblight(LMPOFF, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPON)
		lcd_message("Green Light!", "")
		phase = 1
	else:
		phase = 1
		log_message("Not a valid phase")
	
	return phase


def controlring1(phase):
# RUN NORMAL SEQUENCE FOR NORTHBOUND AND EASTBOUND LIGHT

# phase 0 - do nothing
# phase 1 - nb cg, eb cr
# phase 2 - nb cy, eb cr
# phase 3 - nb cr, eb cr
# phase 4 - nb cr, eb cg
# phase 5 - nb cr, eb cy
# phase 6 - nb cr, eb cr
	debug_message("incoming phase: " + str(phase))
	nextphase = 0

	if phase == 0:
		log_message("Doing nothing")
	elif phase == 1:
		log_message("NB GRN -- EB RED")
		nblight(LMPOFF, LMPOFF, LMPON, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		nextphase = 2
	elif phase == 2:
		log_message("NB YEL -- EB RED")
		nblight(LMPOFF, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		nextphase = 3
	elif phase == 3:
		log_message("NB RED -- EB RED")
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		nextphase = 4
	elif phase == 4:
		log_message("NB RED -- EB GRN")
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPON)
		nextphase = 5
	elif phase == 5:	
		log_message("NB RED -- EB YEL")
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPON, LMPOFF)
		nextphase = 6
	elif phase == 6:
		log_message("NB RED -- EB RED")
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		nextphase = 1
	else:
		nextphase = 1

	debug_message("Outgoing phase: " + str(nextphase))
	return nextphase

def controlring2(phase):
# NORMAL SEQUENCE FOR CONTROLLING NORTHBOUND AND SOUTHBOUND TRAFFIC
# phase 0 - do nothing
# phase 1 - nb cg, sb cg
# phase 2 - nb cy, sb cy
# phase 3 - nb cr, sb cr
# phase 4 - nb cg lg, sb cr
# phase 5 - nb cg ly, sb cr 

	if phase == 0:
		log_message("Doing nothing")
	elif phase == 1:
		nblight(LMPOFF, LMPOFF, LMPON, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPOFF, LMPON)
		phase = 2
	elif phase == 2:
		nblight(LMPOFF, LMPON, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPOFF, LMPON, LMPOFF)
		phase = 3
	elif phase == 3:
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 4
	elif phase == 4:
		nblight(LMPOFF, LMPOFF, LMPON, LMPOFF, LMPON)
		eblight(LMPOFF, LMPOFF, LMPOFF)
		phase = 5
	elif phase == 5:
		nblight(LMPOFF, LMPOFF, LMPON, LMPON, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		phase = 1
	else:
		log_message("Invalid phase")
		phase = 1
	return phase 

def randomspeed():
	speed=random.randint(25,50)
	return speed

def eightball():
# run the magic 8 ball game with the traffic light 
	rand=random.randint(1,3)

	display_message("Ask as question", "3...")
	sleep(1)
	display_message("Ask as question", "2...")
	sleep(1)
	display_message("Ask as question", "1...")
	sleep(1)

	if rand == 1:
		eblight(LMPON, LMPOFF, LMPOFF)
	elif rand == 2:
		eblight(LMPOFF, LMPON, LMPOFF)
	elif rand == 3:
		eblight(LMPOFF, LMPOFF, LMPON)
	else:
		log_message("Invalid Phase")

def allon(phase):
# TURNS ON THE LIGHTS BASED ON THE ARGUMENT PROVIDED 
	if phase == "all":
		nblight(LMPON, LMPON, LMPON, LMPON, LMPON)
		eblight(LMPON, LMPON, LMPON)
		lcd_message("ALL LIGHTS ON", "")
	elif phase == "red":
		nblight(LMPON, LMPOFF, LMPOFF, LMPOFF, LMPOFF)
		eblight(LMPON, LMPOFF, LMPOFF)
		lcd_message("ALL REDS ON", "")
	elif phase == "yellow":
		nblight(LMPOFF, LMPON, LMPOFF, LMPON, LMPOFF)
		eblight(LMPOFF, LMPON, LMPOFF)
		lcd_message("ALL YELLOWS ON", "")
	elif phase == "green":
		nblight(LMPOFF, LMPOFF, LMPON, LMPOFF, LMPON)
		eblight(LMPOFF, LMPOFF, LMPON)
		lcd_message("ALL GREENS ON", "")
	else:
		log_message("Doing nothing")
		
	sleep(3)
	display.lcd_clear()

def alloff():
# TURNS OFF ALL OF THE LIGHTS
	lcd_message("ALL LIGHTS OFF", "")
	for i in pinOutList:
		light_off(i)
	sleep(3)
	display.lcd_clear()

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
	display.lcd_clear()

def mainmenu():
# MAIN MENU FOR THE PROGRAM
    os.system('clear')
    
    print "Main Menu\n"
    print "1) All Lights On\n"
    print "2) All Lights Off\n"
    print "Q) Exit\n"

    selection = raw_input(">> ")

    if selection == "1"
        allon
    elif selection == "2"
        alloff
    elif selection == "3"
        
    elif selection == "Q":
        sys.exit()
