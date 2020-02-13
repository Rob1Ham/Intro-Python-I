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
import calendar
from datetime import datetime

argv = sys.argv


def custom_calendar(*argv):
  if len(argv) == 1:
    return calendar.prmonth(datetime.today().year, datetime.today().month)
  elif len(argv) == 2:
    return calendar.prmonth(datetime.today().year, int(argv[1]))
  elif len(argv) == 3:
    return calendar.prmonth(int(argv[1]), int(argv[2]))
  else:
    return "This program accepts 0-2 arguments. Too many arguments inputted. No inputs returns current month/year. One input specifies the month, two specifies month and year."

print(custom_calendar(*argv))
