from utilities import utility

n = int(input("Enter the size of list\n"))
ch = int(input("Enter the Choice"))
if ch == 1:
    utility.BinaySearchInteger(n)
elif ch == 2:
    utility.BinaySearchString(n)
elif ch == 3:
    utility.InsertionSortInteger(n)
elif ch == 4:
    utility.InsertionSortString(n)
elif ch == 5:
    utility.BubbleSortInteger(n)
elif ch == 6:
    utility.BubbleSortString(n)
else:
    print("Enter the Valid Choice")
