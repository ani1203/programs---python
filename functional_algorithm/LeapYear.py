# I/P -> Year, ensure it is a 4 digit number.
# Logic -> Determine if it is a Leap Year.
# O/P -> Print the year is a Leap Year or not.

from utilities import utility

try:
    year = int(input("enter year you wan to check as leap year"))
    utility.leap_year(year)
except Exception as e:
    print("enter the year in the form of digits")


