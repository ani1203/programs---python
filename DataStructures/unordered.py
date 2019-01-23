from ds.utilities.utility import *


def unordered_list():
    """
    THIS METHOD IS USED TO READ THE FILE AND APPEND
    OR REMOVE THE STRING FILE DATA
    """

    obj1 = LinkedList()  # creating the object of the Linked list class
    try:
        file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/anil.txt", "r+")

        list1 = file.readlines()        # function to read the lines inside the file

        file_string = list1[0]

        list1 = file_string.split()     # splitting the elements into individual elements

        for i in range(0, len(list1)):

            obj1.append(list1[i].strip())  # stripping the white spaces and appending the elements

        file.close()

        print("These are the data that we have in our File\n")

        file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/anil.txt", "r+")

        list1 = file.readlines()

        list1 = list1[0]

        print(list1)                      # printing the list1

        file.close()
    except Exception as e:                 # giving exceptions for validation
        print(e)
    try:

        data = input("Enter data you are looking for:\n")

    except Exception as e:                  # giving exceptions for validation

        print(e)

        print("Enter string only")

    print(obj1.search_item(data))           # calling the function

    print("The updated file content are as follows\n")

    obj1.file_update(data)


if __name__ == '__main__':

    unordered_list()                # calling the method inside the main mehtod
