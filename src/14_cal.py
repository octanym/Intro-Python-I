"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to
print out a calendar for April in 2015, but if you omit either the year or both values,
it should use today’s date to get the month and year.
"""

import sys
# DONT import argparse
import calendar
from datetime import datetime

"""
accepts input of 2 ints
sys.argv[1], sys.argv[2]

if you omit the args, then print datetime current time

if only one arg is passed assume it is the month and default the year arg to 2020

if 2 args are passed in assume month is arg[0] and year is arg[1] and render the calendar for that month and year

if the only arg passed is not coherent to a monthly int, return a usage statement


"""

yy = 2020
mm = 7
dd = 13
dt = datetime(yy, mm, dd)
today = dt.today()
# month = calendar.month(yy, args[1])
# sys.argv is a list of the arguments as strings
sysargs = [i for i in sys.argv]
inputlength = len(sysargs)

curryear = datetime.now().year
currmonth = datetime.now().month


def whats_the_date(args):
    if inputlength == 1:
        calendarcurr = calendar.month(curryear, currmonth)
        print(calendarcurr)
    elif inputlength == 2:
        month = int(args[1])
        calendarmonth = calendar.month(curryear, month)
        print(calendarmonth)
    elif inputlength == 3:
        month = int(args[1])
        year = int(args[2])
        calendarmonthyear = calendar.month(year, month)
        print(calendarmonthyear)
    else:
        print("acceptable inputs should be formatted as mm yyyy")


whats_the_date(sysargs)
