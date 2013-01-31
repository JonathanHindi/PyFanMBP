# PyFanMBP - Python Fan Controller for MBP with GTK interface.
**This app is not for production use.** 
- Just created for fun.
- Planning to revisit the code. 
- First app to create using Python for me. 

## Requirements
- Linux
- MacBook Pro 13"
- Python 2.7
- GTK

## Features
- Simple UI Slider.
- Support only 13" Macbook pro for now. (1 CPU Fan)

## Usage
- Clone the repo to your machine. 
- Open your terminal
- Run `sudo -i`
- Write your password.
- Navigate to directoty. 
- Run `./PyFanMBP.py`, Make sure that the file is executable before doing so. 

## Purpose
- For Educational Purpose Only.


## Roadmap and ToDo
- HTML5/CSS3 Interface using [tideSDK](http://www.tidesdk.org/)
- Support for 15" and 17" Macbook Pro with 2 CPU Fans.
- Verify that using on MacBook Pro and Fan driver is installed before running. 
- Create a .deb package
- Run using Unity/Gnome insted of Terminal.
- Create a Unity Applet. 
- View current CPU temp from sensors. Maybe lm-sensors package will help.  
- Instead of running os.system to change fan value, Change file content using native python lib.
- Get current rpm value and set it as default slider value when launching the app. 
- Validate changes, and display error message if can't set the rpm. 

