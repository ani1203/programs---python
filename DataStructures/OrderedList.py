from ds.utilities.utility import *


def ordered_list():
    """
    THIS METHOD IS USED TO READ FILE AND APPEND OR DELETE
    THE INTEGER DATA FROM THE FILE
    """
    global res
    obj = OrderedList()       # creating the object of the ordered list class
    l2 = []
    res = []
    file = open("./number.txt", "r+")

    list1 = file.readlines()  # using the inbuilt functions to read the lines inside the files

    file_string = list1[0]

    list1 = file_string.split()  # splitting the line list into individual elements
    for i in range(0, len(list1)):
        l2.append(list1[i].strip())  # stripping the white spaces out from the string
    file.close()
    res = [int(i) for i in l2]
    res.sort()
    for j in l2:
        obj.add(j)                  # adding the elements inside

    print("These are the data that we have in our File")
    print(res)                         # printing the result

    try:
        data = str(input("Enter data you are looking for:"))  # enter the data in string form only
    except Exception as e:
        print(e)
        print("Enter string only")      # giving the exceptions for validation
    print(obj.search_item(data))

    print("The updated file content are as follows")
    obj.file_update(data)               # displaying the updated file


if __name__ == '__main__':
    ordered_list()                 # calling the method inside the main method
