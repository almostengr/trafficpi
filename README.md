# Raspi Traffic Control

## Table of Contents
* Purpose
* [System Requirements](#system-requirements)
* Pin Setup
* Running the Scripts
* Known Bugs
* [Bug Reports](#bug-reports)
* Authors
* License
* Acknowledgements
* More Information

----

## Purpose 
The purpose of this project is to educate children about the STEM (Science, Technology, 
Engineering, and Mathematics) fields. Through the use of low cost devices and effective 
teaching, by grouping these subjects together, children are able to associate what they 
are learning with interactions with everyday items. For example, most children are 
aware of the purpose of a traffic light, but most are not aware of a traffic lights' 
internal workings. This project is designed to educate children by explaining the 
workings of the "black box" of a traffic light. This project targets the "T, E, and 
M" of "STEM" by using electronic circuits for controlling the lights, software for 
controlling the electronic circuits, and mathematical calculations for making 
timing decisions.

----

## System Requirements
* Raspiberry Pi 3 (May work on other models, but has been tested on Raspberry Pi 3)
* 8 Channel Relay board (optional)
* Traffic Light (actual or DIY)
* I2C 16x2 LCD Display
* Breadboard Jumper Cables
* Python 2.7.9
* Raspbian Jessie (May work on other OSs, but has only been tested on Raspbian Jessie)

----

## Pin Setup
*To be provided.*

----

## Running The Scripts
To run the script, browse to the script folder, and run `python <scriptname>` where `<scriptname>` is the name of the script.

----

## Known Bugs
* When exiting the script (using Ctrl+C), all of the relays may not turn off. In addition, the LCD display may not clear if it is writing when the kill shortcut is performed.
----

## Bug Reports
Please open a new issue on this repo. Include as much detail that you have so that the issue can be replicated.

----

## Authors
Kenny Robinson, Bit Second Tech

----

## License
This project is licensed under the MIT License.  See LICENSE for more details.

----

## Acknowledgements
* LCD Dipslay code for controlling the LCD display were provided from https://github.com/the-raspberry-pi-guy/lcd. 
* Attempts to replicate the Traffic Light Simulation created by Samuel Vidal seen at https://www.youtube.com/watch?v=xqZRDtX64UA influenced this project.

----

## Road Map
Future enhancements and updates to the scripts will be tracked using the Issue queue.  Any special requests can be submitted. 

----

## More Information
For more information about the author of this script, please visit http://www.bitsecondtech.com.
