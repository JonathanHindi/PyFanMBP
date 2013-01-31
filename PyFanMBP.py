#!/usr/bin/env python

from gi.repository import Gtk
import os
import sys

# Checking if user is root if not promp gksudo
euid = os.geteuid()

if euid != 0:
    args = ['gksudo', sys.executable] + sys.argv + [os.environ]
    # the next line replaces the currently-running process with the sudo
    ('gksudo', args)

# Setting default value for rpmValue
rpmValue = 3000

# Change Fan Mode to manual on start
os.system('sudo echo 0 > /sys/devices/platform/applesmc.768/fan1_manual')


class Handler:
    def gtk_main_quit(self, *args):
        Gtk.main_quit(*args)

    def setRPM(self, button):
    	os.system('sudo echo ' + str(rpmValue) + ' > /sys/devices/platform/applesmc.768/fan1_min')
    	noticationSucess = "notify-send 'Succesfully changed Fan to " + str(rpmValue) + " RPM '"
        os.system(noticationSucess)
  
    def openAbout(self, *arg):
    	about = builder.get_object("AboutDialog")
    	about.show_all()

    def closeAbout(self, *arg):
    	about = builder.get_object("AboutDialog")
    	about.hide()

    def sliderValue(self, scale, value, widget):
    	global rpmValue
    	
    	if widget >= 6000:
    		rpmValue = 6000

    	elif widget <= 2000:
    		rpmValue = 2000

    	else:
    		rpmValue = ('%.0f' % widget)


builder = Gtk.Builder()
builder.add_from_file("PyFanMBP.glade")
builder.connect_signals(Handler())
window = builder.get_object("PyFanMBP")
window.show_all()
Gtk.main()
