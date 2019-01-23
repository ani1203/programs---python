from utilities import utility

try:
    N = int(input("enter the value of N"))
    utility.power_table(N)
except Exception as e:
    print("enter the value of n in digits only")

