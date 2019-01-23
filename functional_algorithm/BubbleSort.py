from utilities import utility
arr = []
arr_size = int(input("enter list size\n"))
print("enter the list elements")
for i in range(0, arr_size):
    arr.append(eval(input()))
utility.bubble(arr)
