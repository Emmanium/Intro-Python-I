"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
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
"""

import sys
import calendar
from datetime import datetime

# Establish Variables for usage later
# The except is there in case someone doesn't enter in a valid number
try:
    user_yy = int(input('Enter the year:'))
except:
    user_yy = None
try:
    user_mm = int(input('Enter the month:'))
except:
    user_mm = None

curr_yy = datetime.now().year
curr_mm = datetime.now().month

# If the user input is longer than 4 digits for the year or 2 for the month
# The program will break
# Print a message explaining the expected format for arguments to be passed in by User annd
# Stop the program
if len(str(user_yy)) > 4 or len(str(user_mm)) > 4:
    print("Put in only four numbers for the year'\nHere's an example: 2020")
    print("Put in two numbers for the month\nHere's an example: 12")
    exit()

# If no input
# Print current month (datetime module)
if user_yy is None and user_mm is None:
    print(calendar.month(curr_yy, curr_mm))

# Else f only one input and not the other:
# Render the current month of the current year
elif user_yy is None and user_mm is not None:
    print(calendar.month(curr_yy, user_mm))
elif user_yy is not None and user_mm is None:
    print(calendar.month(user_yy, curr_mm))

# ElSE both inputs are filled
# Render current month and year
else:
    print(calendar.month(user_yy, user_mm))
