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

dt = datetime(year=2020, month=7, day=10)
today = dt.today()

# mm = sys.argv[1]
# yyyy = sys.argv[2]

# mmyyyy = [int(i) for i in sys.argv if int(i) > 0]

# sys.argv is a list of strings

sysargs = [i for i in sys.argv]


def whats_the_date(args):
    if len(args) == 1:
        # ([filename])
        print("current calendar month")
    elif len(args) == 2:
        # args = ([filename, mm])
        print("calendar of month 'mm' for current year")
        # check if value of mm is less than 12
    elif len(args) == 3:
        # args = ([filename, mm, yyyy])
        # check if value of mm is less than 12
        # check if value of yyyy is less than 2020
        print("that month and year")
    else:
        print("acceptable inputs should be formatted mm yyyy")


whats_the_date(sysargs)

# # try setting sysargs to a list comprehension
# # intuition was correct - this was the solution! nice job!
# # now you just need to implement the detail of the behavior
# # NOTE args gets formatted as an array in a tuple
# # pick up at declaring formatting rules
