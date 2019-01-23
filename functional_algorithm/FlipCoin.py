from utilities import utility


try:
    flip = int(input("enter the no. of times u want to flip the coin"))
    utility.flip_coin(flip)
except ValueError:
    print("give the input as digits only")

