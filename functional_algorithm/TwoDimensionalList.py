from utilities import utility
rows = int(input("enter the rows\n"))
col = int(input("enter the columns\n"))
a = [[0 for i in range(col)] for j in range(rows)]
utility.list_2d(a, rows, col)
