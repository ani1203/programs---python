from utilities import utility
try:
    a = int(input("enter the value of a\n"))
    b = int(input("enter the value of b\n"))
    c = int(input("enter the value of c\n"))
    utility.roots(a, b, c)
except Exception as e:
    print("enter the valid values such that value of b should be greater than a and c")
