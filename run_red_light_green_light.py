#!/usr/bin/python

################################################################################
# Project: 	Rapsi Traffic Control
# Script Usage: run_red_light_green_light.py
# Created: 	2017-05-07
# Author: 	Kenny Robinson, Bit Second Tech (www.bitsecondtech.com)
# Description:	Red Light, Green Light game done with the traffic light. 
################################################################################

import raspitraffic as rtc
from random import randint
from time import sleep

try:
        rtc.setup()
	phasenum=1

        while True:
                red_time=randint(2, 10)
		green_time=randint(0,3)

		phasenum=rtc.controlredlightgreenlight(phasenum)
		rtc.debug_message("Red Time: " + str(red_time))
		sleep(red_time)
			
		phasenum=rtc.controlredlightgreenlight(phasenum)
		rtc.debug_message("Green Time: " + str(green_time))
		sleep(green_time)	

except KeyboardInterrupt:
	rtc.terminate()
