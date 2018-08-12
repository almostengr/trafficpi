# Raspi Traffic Control

## Table of Contents
* Purpose
* System Requirements
* Pin Setup
* Initial Setup
* Running the Scripts
* Uninstall Script
* Bug Reports
* Acknowledgements
* License

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

## Parts List
Below are the list of parts needed for this project. You'll need to choose one of 
the mentioned options below depending on your budget. Using LEDs is cheaper than 
getting an actual traffic light.

* Raspiberry Pi 3 (May work on other models, but has been tested on Raspberry Pi 3)
* Raspiberry Pi power suppy
* Micro SD card (to run the OS)
* USB keyboard (mouse optional)
* HDMI display
* I2C 16x2 LCD Display 
* Breadboard Jumper Cables
* Breadboard (optional)
* Python 2.7.9 (May work with later versions, but has only be tested with 2.7.9)
* Raspbian Jessie (May work on other OSs, but has only been tested with Raspbian Jessie)

### LED Option
* Red LED
* Yellow LED
* Green LED

### Real Traffic Light Option
* Relay board(s) with at least 3 channels
* Traffic Light (actual or replica)

----

## Pin Setup
Below is the mapping for the connections to the Raspberry Pi. The Pin numbers
listed are the physical pin numbers on the board, not the GPIO pin numbers. If 
you are not using a relay board, the connections can be made directly to a 
breadboard with LEDs connected.

* Pi Pin (Board) -------- Device Pin / LED Color
* 2 --------------------- LCD Display VCC (+5V)
* 3 --------------------- LCD Display SDA
* 4 --------------------- Relay Board VCC (+5V)
* 5 --------------------- LCD Display SLC
* 19 -------------------- Red Signal
* 21 -------------------- Yellow Signal
* 23 -------------------- Green Signal
* 30 -------------------- LCD Display GND
* 34 -------------------- Relay Board GND

Visual of Pin Connections to Relay Board
![Image of connections on Raspberry Pi board](https://raw.githubusercontent.com/bitsecondal/raspitraffic-stem/master/docs/circuitry.jpg)

----

## Initial Setup
### Install Script
In the ```scripts``` directory, run the ```install.sh``` script 
as root user. This will install of the required software and python packages.

### Update Apache Configuration
Search for the file containing "PrivateTmp=true". This file should be in your /etc
directory. Change this value to ```PrivateTmp=false```. Then restart Apache.
You may use 
```sh
cd /etc/
grep -R "PrivateTmp=true" *
```
to search for the file that contains this value. Once grep returns the file name, 
edit the file and make the stated change.

----

## Running The Scripts
To control the traffic light, visit the webpage in your browser. A form will be 
presented with a list of programs to select from. Select the program you wish to 
run and click the "Submit" button.

----

## Uninstall Script
At any point, you can uninstall the software that is used by the program to return 
your Raspberry Pi to its prior state. In the ```scripts``` directory, run the 
```uninstall.sh``` script as root user. This will uninstall the packages installed 
by the install script.

----

## Bug Reports and Road Map
Future enhancements, defects, and updates to the scripts are tracked using the 
issue tracker on this repository. For bugs, please include as much detail 
as possible so that the issue can be replicated. Special requests are 
welcome to be submitted.

----

## Known Bugs
* When exiting the script (using Ctrl+C), all of the relays may not turn off.
In addition, the LCD display may not clear if it is writing when the kill
shortcut is performed.

----

## Acknowledgements
* Author: Kenny Robinson, Almost Engineer @almostengr
* LCD Display code for controlling the LCD display were provided from 
https://github.com/the-raspberry-pi-guy/lcd. 
* Attempts to replicate the Traffic Light Simulation created by Samuel Vidal 
seen at https://www.youtube.com/watch?v=xqZRDtX64UA influenced this project.

----

## License
This project is licensed under the MIT License. See LICENSE for more details.

