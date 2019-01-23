from utilities import utility
a = []
a_size = int(input("enter list size\n"))
print("enter the list elements")
for i in range(0, a_size):
    a.append(input())
utility.sort1(a)
