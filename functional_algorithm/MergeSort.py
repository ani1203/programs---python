from utilities import utility
arr = []
arr_size = int(input("enter the size\n"))
print("enter the elements")
for i in range(0, arr_size):
    arr.append(eval(input()))
utility.mergeSort(arr)
print(arr)
