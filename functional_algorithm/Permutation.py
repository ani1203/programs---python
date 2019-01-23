from utilities import utility
string = input("enter the string")  # getting the string from the user
n = len(string)  # getting the length of the user-input string
a = list(string)  # converting the string to list to get the indexes of the string to swap the letters of it
utility.permute(a, 0, n-1)