"""
you'll create a calculator than can compute the area of a given shape, as selected by the user. The calculator will be able to determine the area of the following shapes:

Circle
Triangle
"""
from math import pi
from time import sleep
from datetime import datetime

now=datetime.now()
print "calculating"
print "Current time: %s/%s/%s %s:%s" % (now.month, now.day, now.year, now.hour, now.minute)
sleep(1)
hint="Don't forget to include the correct units! \nExiting..."
option=raw_input("enter C for circle or T for Triangle: ")
if option.upper() =="C":
    radius=float(raw_input("please enter the radius:"))
    area=pi*(radius**2)
    print "The pie is baking..."
    sleep(1)
    print "area is %.2f. \n%s:" %(area,hint)
elif option.upper()=="T":
    base=float(raw_input("please enter the base: "))
    height=float(raw_input("please enter the height:"))
    area=(base*height)/2
    print "The boob is here..."
    sleep(1)
    print "area is %.2f. \n%s:"%(area,hint)
else:
    print "Invalid request"
    
