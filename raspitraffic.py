#!/usr/bin/python

################################################################################
# Project: Raspi Traffic Control
#
# Script Usage: raspitraffic.py
#
# Created: 2017-04-02
#
# Author: Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
#
# Description:Core script which all the functions for controlling the lights
# are contained. 
################################################################################

from time import sleep
from random import randint
import RPi.GPIO as GPIO
import lcddriver
import random
import sys
import os

# DEBUGGING MODE, DISABLED=0, ENABLED=1
DEBUG=0

# LIST ALL OF THE PINS USED
# pinOutList = [37, 35, 33, 31, 29, 23, 21, 19]
pinOutList = [23, 21, 19]

# DEFINE THE GPIO NUMBERS AND VARIABLES FOR THE EASTBOUND TRAFFIC
EAST_CR = 23
EAST_CY = 21
EAST_CG = 19

# DEFINE CONSTANTS
LAMPON=GPIO.LOW
LAMPOFF=GPIO.HIGH
ALL_RED_TIME=2
FLASHER_DELAY=.7

display=lcddriver.lcd()
selection=0


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

    sleep(1)

    # turn off all the lights
    for i in pinOutList:
        GPIO.output(i, GPIO.HIGH)

    # log_message("Done performing setup")
    lcd_message("Done performing setup", "")

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
# print message on computer screen
    print message
    return 0


def lcd_message(line1, line2):
# Displays the message on the LCD screen and computer screen
    display.lcd_clear()
    display.lcd_display_string(line1, 1)
    display.lcd_display_string(line2, 2)
    # log_message(line1 + " | " + line2)
    return 0


def terminate():
# WHEN COMMAND TO EXIT IS GIVEN, THEN RESET EVERYTHING BACK TO DEFAULT
    log_message("Exiting")
    GPIO.cleanup()
    display.lcd_clear()
   

def run_red_light_green_light():
# SEQUENCE FOR RED LIGHT GREEN LIGHT GAME.

    # phase 0 - do nothing
    # phase 1 - red light
    # phase 2 - green light
    
    phasenum=1

    while True:
        red_time=randint(2, 10)
	    green_time=randint(1, 3)

	    phasenum=rtc.controlredlightgreenlight(phasenum)
	    rtc.debug_message("Red Time: " + str(red_time))
	    rtc.lcd_message("Red Light!", "Dont move!")
	    sleep(red_time)
		
	    phasenum=rtc.controlredlightgreenlight(phasenum)
	    rtc.debug_message("Green Time: " + str(green_time))
	    rtc.lcd_message("Green Light!", "Run!")
	    sleep(green_time)

        
def run_signal(country):
# runs the light using normal signal
    while True:
        phasering1=1
        phaseflasher=0

        east_grn_time=random.randint(7, 60)
        east_yel_time=random.randint(2, 5)
        east_red_time=random.randint(7, 60)

        # red
        eblight(LAMPON, LAMPOFF, LAMPOFF)
        for ttime in range(east_red_time, 0, -1):
	        lcd_message("Red", "Time Remain: " + str(ttime) + "s")
	        sleep(1)
	        
	    if country == "UK":
            eblight(LAMPON, LAMPON, LAMPOFF)
            for ttime in range(east_yel_time, 0, -1):
	            lcd_message("Red-Yellow", "Time Remain: " + str(ttime) + "s")
	            sleep(1)
	        
        # green 
        eblight(LAMPOFF, LAMPOFF, LAMPON)
        for ttime in range(east_grn_time, 0, -1):
	        lcd_message("Green", "Time Remain: " + str(ttime) + "s")
	        sleep(1)

        # yellow
        eblight(LAMPOFF, LAMPON, LAMPOFF)
        # for ttime in range(int(round(north_yel_time, 0)), 0, -1):
        for ttime in range(east_yel_time, 0, -1):
	        lcd_message("Yellow", "Time Remain: " + str(ttime) + "s")
	        sleep(1)
	        
        # red
        # phasering1=controlring1(phasering1)
        eblight(LAMPON, LAMPOFF, LAMPOFF)
        for ttime in range(east_red_time, 0, -1):
	        lcd_message("Red", "Time Remain: " + str(ttime) + "s")
	        sleep(1)

        # change flasher color
        if phaseflasher == 1 or phaseflasher == 2:
            phaseflasher = 3
        else:
            phaseflasher = 1

        # flasher
        for i in 20:
            phaseflasher = controlflasher(phaseflasher)
            sleep(1)


def controlflasher(phase):
# runs flasher sequence

    if phase == 0:
        log_message("Do nothing")

    # flash red
    elif phase == 1:
        # nblight(LAMPOFF, LAMPON, LAMPOFF, LAMPOFF, LAMPOFF)
        eblight(LAMPOFF, LAMPOFF, LAMPOFF)
        # lcd_message("Flasher Mode", "EB OFF, NB YEL")
        phase=2
    elif phase == 2:
        # nblight(LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF)
        eblight(LAMPON, LAMPOFF, LAMPOFF)
        # lcd_message ("Flasher Mode", "EB RED, NB OFF")
        phase=1

    # # flash red lights
    # elif phase == 3:
    # # nblight(LAMPON, LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF)
    # eblight(LAMPOFF, LAMPOFF, LAMPOFF)
    # phase=4
    # elif phase == 4:
    # # nblight(LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF)
    # eblight(LAMPON, LAMPOFF, LAMPOFF)
    # phase=3

    # flash yellow lights
    elif phase == 5:
        # nblight(LAMPOFF, LAMPON, LAMPOFF, LAMPOFF, LAMPOFF)
        eblight(LAMPOFF, LAMPOFF, LAMPOFF)
        phase = 6
    elif phase == 6:
        # nblight(LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF)
        eblight(LAMPOFF, LAMPON, LAMPOFF)
        phase = 5

    # flash green lights
    elif phase == 7:
        # nblight(LAMPOFF, LAMPOFF, LAMPON, LAMPOFF, LAMPON)
        eblight(LAMPOFF, LAMPOFF, LAMPOFF)
        phase = 8
    elif phase == 8:
        # nblight(LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF)
        eblight(LAMPOFF, LAMPOFF, LAMPON)
        phase = 7

    # # flash with nb red, eb yellow
    # elif phase == 9:
    # # nblight(LAMPON, LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF)
    # eblight(LAMPOFF, LAMPOFF, LAMPOFF)
    # phase = 10
    # elif phase == 10:
    # # nblight(LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF)
    # eblight(LAMPOFF, LAMPON, LAMPOFF)
    # phase = 9

    else:
        log_message("Not valid flasher phase")
        phase = 0

    return phase


def calc_yellow_time( speed, grade ):
# CALCULATE THE AMOUNT OF YELLOW LIGHT TIME
    yel_time = 1 + ((1.47 * speed) / (2 * (10 + (0 / 100) * 32.2)))
    # log_message("Yellow Time: " + str(yel_time))
    return yel_time


def calc_green_time():
# SET A RANDOM VALUE FOR THE GREEN TIME
    grn_time=random.randint(10, 45)
    # log_message("Green Time: " + str(grn_time))
    return grn_time


def eblight(cirred, ciryel, cirgrn):
# CONTROLS THE LAMPS ON THE EASTBOUND LIGHT. DOESNT HAVE LEFT TURN
    GPIO.output(EAST_CR, cirred)
    GPIO.output(EAST_CY, ciryel)
    GPIO.output(EAST_CG, cirgrn)	


def randomspeed():
# picks a random speed from the range defined below
    speed=random.randint(25,65)
    return speed
    

def run_eightball():
# run the magic 8 ball game with the traffic light 

    # display prompts
    lcd_message("Ask as question", "3...")
    sleep(1)
    lcd_message("Ask as question", "2...")
    sleep(1)
    lcd_message("Ask as question", "1...")
    sleep(1)

    # pick a random number
    rand=random.randint(1,3)

    if rand == 1:
        eblight(LAMPON, LAMPOFF, LAMPOFF)
        lcd_message("No","")
    elif rand == 2:
        eblight(LAMPOFF, LAMPON, LAMPOFF)
        lcd_message("Maybe", "")
    elif rand == 3:
        eblight(LAMPOFF, LAMPOFF, LAMPON)
        lcd_message("Yes", "")
    else:
        log_message("Invalid Phase")


def allon(phase):
# TURNS ON THE LIGHTS BASED ON THE ARGUMENT PROVIDED 
    if phase == "all":
        # nblight(LAMPON, LAMPON, LAMPON, LAMPON, LAMPON)
        eblight(LAMPON, LAMPON, LAMPON)
        lcd_message("ALL LIGHTS ON", "")
    elif phase == "red":
        # nblight(LAMPON, LAMPOFF, LAMPOFF, LAMPOFF, LAMPOFF)
        eblight(LAMPON, LAMPOFF, LAMPOFF)
        lcd_message("ALL REDS ON", "")
    elif phase == "yellow":
        # nblight(LAMPOFF, LAMPON, LAMPOFF, LAMPON, LAMPOFF)
        eblight(LAMPOFF, LAMPON, LAMPOFF)
        lcd_message("ALL YELLOWS ON", "")
    elif phase == "green":
        # nblight(LAMPOFF, LAMPOFF, LAMPON, LAMPOFF, LAMPON)
        eblight(LAMPOFF, LAMPOFF, LAMPON)
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

    log_message("Main Menu")
    log_message("====================")
    log_message("1) All Lights On")
    log_message("2) All Lights Off")
    log_message("3) Green On")
    log_message("4) Yellow On")
    log_message("5) Red On")
    log_message("6) Flash Red")
    # log_message("7) Flash Yellow")
    log_message("8) Flash Green")
    log_message("9) Flash Yellow")
    log_message("Q) Exit")
    
    selection = raw_input(">> ")

    return selection


# configure everything
# setup()

# while (selection != "Q"):
while (selection != "Q" or selection != "q"):
    try:
        selection = 0
        selection = mainmenu()

        setup()
        debug_message("Debug mode enabled")

        if selection == "1":
        # all lights on
            allon("all")

        elif selection == "2":
        # all lights off
            alloff()

        elif selection == "6":
        # flash red
            phaseflasher=1
            while True:
                lcd_message("Flashing Red", "")
                phaseflasher=controlflasher(phaseflasher)
                sleep(FLASHER_DELAY)

        elif selection == "7":
        # flash yellow
            phaseflasher=9
            while True:
                lcd_message("Flashing Yellow", "")
                phaseflasher=controlflasher(phaseflasher)
                sleep(FLASHER_DELAY)

        elif selection == "8":
        # flash green
            phasenum=7
            while True:
                lcd_message("Flashing Green", "")
                phasenum=controlflasher(phasenum)
                sleep(FLASHER_DELAY)

        elif selection == "3":
        # green on
            allon("green")

        elif selection == "4":
        # yellow on 
            allon("yellow")

        elif selection == "5":
        # red on 
            allon("red")

        elif selection == "9":
		# flash yellow
            phasenum=5
            while True:
                phasenum=controlflasher(phasenum)
                sleep(FLASHER_DELAY)

        elif selection == "10":

            phaseflasher=0
            phasering1=1
            counter=0
            east_grn_time=0
            east_yel_time=0
            # ALL_RED_TIME=getallredtime()

            while True:
                debug_message("Turning all red")
                east_speedlimit=randomspeed()
                phasering1=controlring1eb(phasering1)

            if counter>0:
                lcd_message("Yellow Time: " + str(east_yel_time) + "s", "Game over")
                sleep(ALL_RED_TIME)

            for x in range(ALL_RED_TIME, 0, -1):
                lcd_message("All Red Delay", "Starting in " + str(x) + "s")
                sleep(1)

            ## BOUNDARY

            east_speedslimit=randomspeed()
            east_grn_time=calc_green_time()

            debug_message("Turning east green")

            phasering1=controlring1eb(phasering1)

            east_yel_time=calc_yellow_time(east_speedlimit, 0)

            for x in range(east_grn_time, 0, -1):
                lcd_message("Speed Limit: " + str(east_speedlimit), "Time Remain: " + str(x) + "s")
                sleep(1)

            debug_message("Turning east yellow")

            # east_yel_time=calc_yellow_time(east_speedlimit, 0)

            phasering1=controlring1eb(phasering1)

            lcd_message("Yellow Time: ", str(east_yel_time) + " seconds")

            sleep(east_yel_time)

            counter=1
            

        elif selection == "11":
            while True:
                phasering1=2

                north_grn_time=randint(5, 15)
                north_yel_time=randint(2, 5)
                east_grn_time=randint(5, 15)
                east_yel_time=randint(2, 5)

                # normal cycle loop
                # for x in range(0, 2, +1):

                # nb green
                phasering1=controlring1uk(phasering1)
                for ptime in range(north_grn_time, 0, -1):
                    lcd_message("Time: " + str(ptime), "")
                    sleep(1)

                # nb yellow
                phasering1=controlring1uk(phasering1)
                for ptime in range(north_yel_time, 0, -1):
                    lcd_message("Time: " + str(ptime), "")
                    sleep(1)

                # all red
                phasering1=controlring1uk(phasering1)
                for ptime in range(ALL_RED_TIME, 0, -1):
                    lcd_message("Time: " + str(ptime), "")
                    sleep(1)

                # eb green 
                phasering1=controlring1uk(phasering1)
                for ptime in range(east_grn_time, 0, -1):
                    lcd_message("Time: " + str(ptime), "")
                    sleep(1)

                # eb yellow
                phasering1=controlring1uk(phasering1)
                for ptime in range(east_yel_time, 0, -1):
                    lcd_message("Time: " + str(ptime), "")
                    sleep(1)

                # all red
                phasering1=controlring1uk(phasering1)
                for ptime in range(ALL_RED_TIME, 0, -1):
                    lcd_message("Time: " + str(ptime), "")
                    sleep(1)

        elif selection == "12":
            # ALL_RED_TIME=getallredtime()
            counter = 0

            while True:
                phasering1=1
                phaseflasher=0

                north_grn_time=calc_green_time()
                north_yel_time=calc_yellow_time(randomspeed(), random.randint(0, 5))
                east_grn_time=calc_green_time()
                east_yel_time=calc_yellow_time(randomspeed(), random.randint(0, 5))

                # nb grn, eb red
                phasering1=controlring1(phasering1)
                for ttime in range(north_grn_time, 0, -1):
                    lcd_message("NB GRN, EB RED", "Time Remain: " + str(ttime) + "s")
                    sleep(1)

                # nb yel, eb red
                phasering1=controlring1(phasering1)
                for ttime in range(int(round(north_yel_time, 0)), 0, -1):
                    lcd_message("NB YEL, EB RED", "Time Remain: " + str(ttime) + "s")
                    sleep(1)

                # all red phase
                phasering1=controlring1(phasering1)
                for ttime in range(ALL_RED_TIME, 0, -1):
                    lcd_message("NB RED, EB RED", "Time Remain: " + str(ttime) + "s")
                    sleep(1)

                # nb red, eb grn
                phasering1=controlring1(phasering1)
                for ttime in range(east_grn_time, 0, -1):
                    lcd_message("NB RED, EB GRN", "Time Remain: " + str(ttime) + "s")
                    sleep(1)

                # nb red, eb yel
                phasering1=controlring1(phasering1)
                for ttime in range(int(round(east_yel_time, 0)), 0, -1):
                    lcd_message("NB RED, EB YEL", "Time Remain: " + str(ttime) + "s")
                    sleep(1)

                # all red
                phasering1=controlring1(phasering1)
                for ttime in range(ALL_RED_TIME, 0, -1):
                    lcd_message("NB RED, EB RED", "Time Remain: " + str(ttime) + "s")
                    sleep(1)

        elif selection == "13":
        ## red light, green light
            phasenum=1
            while True:
                red_time=randint(2, 10)
                green_time=randint(1, 3)

                phasenum=controlredlightgreenlight(phasenum)
                debug_message("Red Time: " + str(red_time))
                # lcd_message("Red Light!", "Dont move!")
                sleep(red_time)

                phasenum=controlredlightgreenlight(phasenum)
                debug_message("Green Time: " + str(green_time))
                # lcd_message("Green Light!", "Run!")
                sleep(green_time)

        elif selection == "Q" or selection == "q":
        # exit the script
            sys.exit()
            # log_message("Exiting...")

        else:
        # display error and help message
            log_message("Invalid selection, try again.")

    except KeyboardInterrupt:
        terminate()
