"""
in this calendar user should be able to choose to:

View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event
"""
from time import strftime,sleep

USER_FIRST_NAME="Xiao"
calendar={}
def welcome():
    print "welcome, ", USER_FIRST_NAME,"."
    print "calendar was opened"
    sleep(1)
    print "Today is: "+ strftime("%A %B %d,%Y")
    print strftime("%H:%M:%S")
    sleep(1)
    print "What would you like to do?"

def start_calendar():
    welcome()
    start=True
    while start:
        user_choice= raw_input( "A to Add, U to Update, V to View, D to Delete, X to Exit:")
        user_choice=user_choice.upper()
        if user_choice=="V":
          if len(calendar.keys())<1:
            print "Calendar empty."
          else:
            print calendar
        elif user_choice=="U":
          date=raw_input("what date?")
          update=raw_input("Enter the update:")
          calendar[date]=update
          print "update succeed"
          print calendar
        elif user_choice=="A":
          event=raw_input("enter event:")
          date=raw_input("enter date(MM/DD/YYYY):")
          if (len(date)>10 or int(date[6:])< int(strftime("%Y"))):
            print "Plase enter a valid date"
            try_again=raw_input("Try again?Y for yes,N for no: ")
            try_again=try_again.upper()
            if try_again=="Y":
              continue
            else:
              start=False
          else:
            calendar[date]=event
            print "event added successfully"
            print calendar
        elif user_choice=="D":
          if len(calendar.keys())==0:
            print "It enpty"
          else:
            event=raw_input("what to delete")
            for date in calendar.keys():
              if event==calendar[date]:
                del calendar[date]
                print "event deleted"
                print calendar
              else:
                print "error"
        elif user_choice=="X":
            start=False
        else:
            print "invalid enter"
            start=False

start_calendar()

