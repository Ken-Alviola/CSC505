# This script uses the calendar library and takes an input of 3 integers on the same line (mm dd yyyy) separated by a space 
# that represents a date and prints the corresponding day of the week

import calendar
print()
n1,n2,n3=map(int,input().split())
print((calendar.day_name[calendar.weekday(n3,n1,n2)]).upper())
print()