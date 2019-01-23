'''
@author
@date
@file
@overview

'''

from ds.utilities.utility import HashTable


def hashing_runner():
    """
    THIS METHOD IS USED TO CREATE A HASHING FUNCTION
    TO SEARCH A NUMBER IN A SLOT
    """

    hash_obj = HashTable()                          # creating the object of the Hashtable class

    print('These are the Numbers in our File')
    file = open("/home/admin1/number.txt", "r")     # opening the file to read using functions
    print(file.readline())
    try:
        number = int(input('Now enter the Number you are looking for: '))
    except Exception as e:                           # putting exception for validation
        print(e)
        print("Enter Number only")
    hash_obj.insert()
    print(hash_obj.search(number))

    print('Now Updated File Content are as Follows')
    hash_obj.file_update(number)                    # calling the functions from the hashtable class


if __name__ == "__main__":                  # calling the method inside the main method
    hashing_runner()
