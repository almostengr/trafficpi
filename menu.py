#!/usr/bin/python

################################################################################
# Project: Raspi Traffic Control
# Script Usage: menu.py
# Created: 2018-03-18 
# Author: Kenny Robinson, @almostengr, www.bitsecondtech.com
# Description: Main menu for use with command line / ssh interface
################################################################################

import trafficcontrol as rtc
import os

selection = 0

def mainmenu():
# MAIN MENU FOR THE PROGRAM
    os.system('clear')

    rtc.log_message("Main Menu")
    rtc.log_message("====================")
    rtc.log_message("1) All Lights On")
    rtc.log_message("2) All Lights Off")
    rtc.log_message("3) Green On")
    rtc.log_message("4) Yellow On")
    rtc.log_message("5) Red On")
    rtc.log_message("6) Flash Red")
    rtc.log_message("8) Flash Green")
    rtc.log_message("9) Flash Yellow")
    rtc.log_message("20) US Signal")
    rtc.log_message("21) UK Signal")
    rtc.log_message("Q) Exit")
    rtc.log_message("")
    rtc.log_message("Use Ctrl+C to exit running command.")

    selection = raw_input(">> ")

    return selection

# while (selection != "Q"):
while (selection != "Q" or selection != "q"):
    try:
        selection = 0
        selection = mainmenu()

        rtc.debug_message("Debug mode enabled")

	# perform setup if not exiting
	if selection != "q" or selection != "Q":
	    rtc.setup()

        if selection == "1":
        # all lights on
            rtc.allon("all")

        elif selection == "2":
        # all lights off
            rtc.alloff()

        elif selection == "6":
        # flash red
            phaseflasher=1
            while True:
                rtc.lcd_message("Flashing Red", "")
                phaseflasher=rtc.controlflasher(phaseflasher)
                sleep(FLASHER_DELAY)

        elif selection == "7":
        # flash yellow
            phaseflasher=9
            while True:
                rtc.lcd_message("Flashing Yellow", "")
                phaseflasher=rtc.controlflasher(phaseflasher)
                sleep(FLASHER_DELAY)

        elif selection == "8":
        # flash green
            phasenum=7
            while True:
                rtc.lcd_message("Flashing Green", "")
                phasenum=rtc.controlflasher(phasenum)
                sleep(FLASHER_DELAY)

        elif selection == "3":
        # green on
            rtc.allon("green")

        elif selection == "4":
        # yellow on
            rtc.allon("yellow")

        elif selection == "5":
        # red on
            rtc.allon("red")

        elif selection == "9":
	# flash yellow
            phasenum=5
            while True:
                phasenum=rtc.controlflasher(phasenum)
                sleep(FLASHER_DELAY)

        elif selection == "20":
        # US signal pattern
            rtc.run_signal("US")

        elif selection == "21":
        # UK signal pattern
            rtc.run_signal("UK")

        elif selection == "Q" or selection == "q":
        # exit the script
            sys.exit()

        else:
        # display.error and help message
            rtc.log_message("Invalid selection, try again.")

    except KeyboardInterrupt:
        rtc.terminate()

