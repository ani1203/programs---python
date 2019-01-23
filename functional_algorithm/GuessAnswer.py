from utilities import utility
n = int(input("how many questions you want to be asked?\n"))
first = 0
last = int(2**n)
print("think of any number between", first, "and", last)
print(utility.number(first, last))
