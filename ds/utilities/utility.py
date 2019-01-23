# @author - anil mehta
# version 3.7
# since - 5th january 2019


# all the methods will be created here and it will be called in the main file of that particular program...

from utilities import utility
import math


class Node:
    """
    class to create node
    This is the constructor of Node class .
    """

    def __init__(self, data, after=None):
        self.data = data
        self.next = after


class LinkedList:
    """
    This class is used to create LinkedList
    """
    head = None

    def __init__(self):
        """
        This is constructor of LinkedList class
        """
        pass

    def append(self, data):
        """
        This method is used to append data given by user at the end of the LinkedList
        """

        node = Node(data)  # node creation

        if self.head is None:

            self.head = node  # if head is null then assign new node to head

        else:

            traverse = self.head

            while traverse.next is not None:  # else traverse pointer till last node and
                traverse = traverse.next  # append new node at end

            traverse.next = node

    def search_item(self, data):
        """
        This method is used to search data given by user.
        """

        traverse = self.head
        if self.head is None:  # execute if list empty
            return False

        while traverse.next is not None:
            if traverse.data == data:  # checks for matching data
                return True
            traverse = traverse.next
        if traverse.data == data:
            return True  # for single node
        else:
            return False

    def remove(self, data):
        """
        This method is used to remove data from the Linked list specified by the use
        """
        global temp
        traverse = self.head
        temp = self.head            # assignments of head
        if self.head is None:
            return None

        if traverse.data == data:
            self.head = traverse.next  # for first node of linked list
            return

        while traverse.next is not None:

            temp = traverse.next
            if temp.data == data:           # matching
                traverse.next = temp.next  # if data match with node then delete
                return

            traverse = traverse.next

    def display(self):
        """
        This method is used to display content of Linked list.
        this method return data present in each node of LinkedList
        and its also useful in HashTable to display each data stored
        in HashTable data structure
        """
        l1 = []
        traverse = self.head

        if self.head is None:
            return None  # if empty then return None

        while traverse.next is not None:
            l1.append(traverse.data)  # append element in list till linked list not end
            traverse = traverse.next

        l1.append(traverse.data)
        return l1  # return Linked List

    def file_update(self, data):
        """
        This method is used to update file after any operation performed on LinkedList
        and it saves the data into the file.
        """
        global l1_content
        file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/anil.txt", "r+")
        file.truncate(0)
        file.close()
        if self.search_item(data) is True:      # search data using search method
            self.remove(data)                   # if found then remove

            file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/anil.txt", "a+")
            l1_content = []
            l1_content = self.display()  # assign linked list to a list
            for i in l1_content:
                file.write(i + " ", )  # write data into file
            file.close()

            file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/anil.txt", "r")
            for i in file:
                print(i)  # print file
            file.close()
        else:
            self.append(data)  # if data not found then append data into file

            file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/anil.txt", "a+")

            l1_content = []
            l1_content = self.display()

            for i in l1_content:
                file.write(i + " ")  # write file data into list
            file.close()

            file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/anil.txt", "r")
            for i in file:
                print(i)  # print list contents
            file.close()

# --------------------------------------------------------------------------------------------------------------------


class Stack:
    """
    This is the Stack class to create Stack.
    """
    top = 0            # Initialization
    head = None

    def __init__(self):
        """
        This is the constructor of Stack class.
        """
        pass

    def push(self, data):
        """
        This method is used to insert data in stack.
        """

        node = Node(data)       # create new node

        if self.head is None:

            self.head = node      # if head is empty then assign new node to head
        else:

            traverse = self.head

            while traverse.next is not None:    # else add to next null position
                traverse = traverse.next

            traverse.next = node

    def size(self):
        """
        This method is used to find the size of Stack.
        """
        traverse = self.head

        if self.head is None:
            return 0
        size = 1
        while traverse.next is not None:    # traverse pointer till last node and
            traverse = traverse.next        # for each node size increment by 1
            size += 1
        return size                     # return count of element in the list

    def show(self):
        """
        This method is used to display content of stack
        """
        traverse = self.head

        if self.top <= -1:      # print message if stack is underflow
            print(" Stack Underflow")
            return
        if traverse is None:
            print("Stack is empty")
            return

        while traverse.next is not None:
            print(traverse.data)        # print element of stack
            traverse = traverse.next
        print(traverse.data)

    def pop(self):
        """
        This method is used to delete last data which is inserted into the stack.
        actually stack follow the Last in First Out order to pop the data from the stack
        """

        traverse = self.head

        if self.head is None:   # if stack empty return -1
            return -1

        if self.head.next is None:
            self.head = None           # if only one element in stack then

            return traverse.data        # set head as none and delete that element and return data

        while traverse.next is not None:

            t1 = traverse.next
            if t1.next is None:             # else delete last node which is top on the stack
                traverse.next = None

                return t1.data
            traverse = traverse.next

    def peek(self):
        """
        This method is used to return the last inserted item in the stack.
        """
        traverse = self.head

        if self.head is None:
            return "empty stack"        # print if stack is empty
        self.top = self.size() - 1
        for i in range(0, self.top):
            traverse = traverse.next    # traverse pointer till last node

        return traverse.data            # return last node which is top element

    def is_empty(self):
        """
        This method is used to know whether stack is empty or not.
        """

        if self.size() == 0:
            return True
        else:
            return False

    def balanced_parentheses(self, string):
        """
        This method is used to check whether expression is balanced or not .
        """
        for i in string:

            if i == '(' or i == '[' or i == '{':
                stack.push(i)                       # adding element into stack

            if ((stack.peek() == '(' and i == ')') or (stack.peek() == '[' and i == ']') or (
                    stack.peek() == '{' and i == '}')) and stack.size() > 0:
                stack.pop()
                continue

        if stack.size() == 0:
            print("Balanced Parenthesis ")      # after push and pop operation if stack size
        else:                                       # is zero then balanced otherwise unbalanced
            print("Parenthesis is not Balanced ")


stack = Stack()
stack1 = Stack()

# ----------------------------------------------------------------------------------------------------------------------


class Queue:
    """
    This Queue class is used to create Queue.
    """
    front = None
    rear = None

    def __init__(self):
        """
        This is the constructor of Queue class .
        """
        pass

    def enqueue(self, data):
        """
        This method is used to insert data in the Queue .
        data will be given by user which data to be inserted ,
        queue follows First in First Out Principle.
        """

        node = Node(data)

        if self.front is None and self.rear is None:

            self.front = node       # front and rear assign to new node
            self.rear = node

        else:

            self.rear.next = node        # else add element in queue by rear
            self.rear = self.rear.next

    def show(self):
        """
        This method is used to display content of queue .
        """

        if self.front is None:
            print("Queue is empty")     # print if queue is empty
            return

        while self.front.next is not None:
            print(self.front.data)          # print queue data
            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):
        """
        This method is used to delete data from the Queue.
        data will deleted according to FIFO principle
        """
        global temp
        temp = self.front
        self.front = self.front.next        # delete data which is pointed by front pointer
        return temp.data                # return deleted data

    def is_empty(self):
        """
       This method is used to know whether Queue is empty or not.
       """
        if self.front is None:
            return True
        else:
            return False

    def size(self):
        """
        This method is used to display content of queue.
        """

        size = 1
        traverse = self.front
        if self.front is None:      # return 0 if queue is empty
            return 0

        while traverse.next is not None:
            traverse = traverse.next        # traverse till last element and count size
            size += 1
        return size


queue = Queue()

# --------------------------------------------------------------------------------------------------------------------


class Deque:
    # used to initialise with the items
    def __init__(self):
        self.items = []

    # used to check whether the Deque is empty or not
    def is_empty(self):
        return self.items == []

    # used to insert an item to the front of the Deque
    def insert_front(self, item):
        self.items.append(item)

    # used to insert an item to the rear of the Deque
    def insert_rear(self, item):
        self.items.insert(0, item)

    # used to remove an item from the front of the Deque
    def remove_front(self):
        return self.items.pop()

    # used to remove an item from the back of the Deque
    def remove_rear(self):
        return self.items.pop(0)

    # used to check the size of the Deque
    def size(self):
        return len(self.items)

# --------------------------------------------------------------------------------------------------------------------------------------


class OrderedList:
    """
    This is used to create OrderedList.
    """
    head = None  # Initialize head as none

    def __init__(self):
        """
        This is the constructor of OrderedList class
        """
        pass

    def add(self, data):
        """
        This method is used to put data in OrderedList in increasing order.
        """
        global temp
        node = Node(data)  # create node
        if self.head is None:  # if list is empty
            self.head = node  # assign node to head

        else:
            traverse = self.head
            if int(self.head.data) > int(node.data):  # compare data before adding it
                self.head = node  # for ascending order if head is greater
                node.next = traverse  # than given data then simply add it.

            if int(self.head.data) < int(node.data):  # if head of data less than new node of data
                temp = self.head
                while traverse.next is not None:
                    if traverse.data < node.data:
                        temp = traverse  # check where new node of data is less than
                    traverse = traverse.next  # next one and if condition satisfy then add

                if traverse.data < node.data:
                    temp = traverse

                temp1 = temp.next
                temp.next = node
                node.next = temp1

    def remove(self, data):
        """
        This method is used to remove data from the OrderedList specified by the user.
        """
        global temp
        traverse = self.head
        temp = self.head
        if traverse.data == data:       # if element found at first position then
            self.head = traverse.next   # increment head and remove that element
            return

        while traverse.next is not None:

            temp = traverse.next
            if temp.data == data:           # search for matching element and remove it
                traverse.next = temp.next
                return

            traverse = traverse.next

    def search_item(self, data):
        """
        This method is used to search data given by user
        """

        traverse = self.head
        while traverse.next is not None:

            if traverse.data == data:  # data matching
                    return True
            traverse = traverse.next
        if traverse.data == data:       # if found return true else return false
            return True
        else:
            return False

    def display(self):
        """
        This method is used to display content of OrderedList.
        this method return each data in each node in LinkedList
         and this method i created so that i can use in HashTable to display
         each data stored in HashTable data structure
        """
        l1 = []
        traverse = self.head

        if self.head is None:     # if list empty
            return

        while traverse.next is not None:
            l1.append(traverse.data)  # append data into list
            traverse = traverse.next

        l1.append(traverse.data)
        return l1                     # return linked list

    def file_update(self, data):
        """
        This method is used to update file after any operation performed on OrderedList
        and it saves the data into the file.
        """
        global l1_content
        file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/number.txt", "r+")
        file.truncate(0)
        file.close()

        if self.search_item(data) is True:              # if element found
            self.remove(data)                           # remove it using remove()
            file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/number.txt", "a+")

            l1_content = []
            l1_content = self.display()    # assign data to list return by
            for i in l1_content:                   # display()  method
                file.write(i + " ", )                   # write data into file
            file.close()

            res = [int(i) for i in l1_content]
            res.sort()      # sort linked list
            print(res)      # print linked list

        else:
            self.add(data)          # if data not found in list then add it

            file = open("/home/admin1/PycharmProjects/BridgeLabz/DataStructures/number.txt", "a+")

            l1_content = []                            # assign data to list return by
            l1_content = self.display()        # display() method
            for i in l1_content:
                file.write(i + " ")                     # write data into file
            file.close()

            res = [int(i) for i in l1_content]
            res.sort()          # sorting of element in ascending order
            print(res)          # print data of linked list

# --------------------------------------------------------------------------------------------------------------------


class HashTable:
    """
    This HashTable class is used to create hashtable data structure.
    """

    def __init__(self):
        pass

    objects_list = []
    for i in range(11):
        """
        creating 11 objects of LinkedList class and storing it in list 
        that is in objects_list to make HashTable data structure
        """
        objects_list.append(LinkedList())

    def hash_function(self, key):
        """
        This method is used to convert users key or data into index.
        this index is used to store user data in hashtable on index which is obtained  by that particular
        data from hash_function
        """
        index = key % len(self.objects_list)
        return index

    def insert(self):
        """
        This method is used to read data from file and convert each data into
        integer format from string format.
        """

        file = open("/home/admin1/number.txt", "r")
        elements = file.readlines()     # read file data
        string = elements[0]

        string_list = string.split()       # split data using split() function

        elements = []
        for i in range(0, len(string_list)):
            to_integer = int(string_list[i])        # append data into list
            elements.append(to_integer)

        for i in range(len(elements)):
            index = self.hash_function(elements[i])         # append element at proper index
            self.objects_list[index].append(elements[i])

    def search(self, data):
        """
        This method is used to search data which is given by user in hashtable data structure.
        """
        index = self.hash_function(data)
        return self.objects_list[index].search_item(data)

    def file_update(self, data):
        """
        This method is used to update file after any operation happened in hashtable
        data structure.
        """
        result = self.search(data)

        if result is True:
            index = self.hash_function(data)
            self.objects_list[index].remove(data)     # if data found then remove it
            self.display_content_hashtable()

        if result is False:
            index = self.hash_function(data)
            self.objects_list[index].append(data)    # if data not fount add it into list
            self.display_content_hashtable()

    def display_content_hashtable(self):
        """
        This method is used to display content of HashTable data structure
        """
        global lines
        file = open("/home/admin1/number.txt", "r+")
        file.truncate(0)
        file.close()
        for i in range(0, len(self.objects_list)):

            if self.objects_list[i].display() is not None:
                lines = []
                lines = self.objects_list[i].display()      # add element into list which returned
                file = open("/home/admin1/number.txt", "a+")   # by display function
                for j in lines:
                    file.write(str(j) + ' ')

        file.close()

        file = open("/home/admin1/number.txt", "r")
        for i in file:
            print(i)
        file.close()

# ---------------------------------------------------------------------------------------------------------------------


class Methods:

    def __init__(self):
        pass

    def calendar(self, month, year):

        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if utility.is_leap(year):      # check leap year
            days[1] = 29
        row = 6
        column = 7
        two_d_array = [[0 for j in range(column)] for i in range(row)]  # create empty 2d array

        print('Your Calender is\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')     # print day's for calender
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:
                    if i == 0 and j < d0:           # while d0 is less than j
                        two_d_array[i][j] = ' '      # it will print blank space
                        continue

                    two_d_array[i][j] = values       # add days into calender
                    values += 1                       # increment counter

        for i in range(row):

            for j in range(column):
                if two_d_array[i][j] != 0:
                    x = two_d_array[i][j]     # method returns the string
                    x1 = str(x).ljust(2)      # left justified in a string of length width.
                    print(x1, end=" ")

            print()

    def calendar_queue(self, month, year):

        """
        This method is used to print calender of given month and year.
        In this method calender is created using queue
        """
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if utility.is_leap(year):     # check leap year
            days[1] = 29
        row = 6
        column = 7

        print('Your Calender is\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')       # print day's for calender
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:       # while d0 is less than j
                    if i == 0 and j < d0:       # it will print blank space
                        queue.enqueue(' ')      # used enqueue() method of queue class
                        continue                # to add space

                    queue.enqueue(values)       # add element in queue
                    values += 1

        for i in range(row):

            for j in range(column):
                if queue.size() > 0:
                    x = queue.dequeue()    # remove element from queue and store it in x variable
                    x1 = str(x).ljust(2)    # using  method print formated calender
                    print(x1, end=" ")
            print()

    def calender_stack(self, month, year):
        """
        This method is used to print calender of given month and year.
        In this method calender is created using stack

        """
        day = ['S', ' M', ' T', ' W', ' Th', 'F', ' S']

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        values = 1
        d = 1

        m = month
        y = year
        y0 = y - (14 - m) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + 31 * m0 // 12) % 7

        if utility.is_leap(year):         # check leap year
            days[1] = 29
        row = 6
        column = 7

        print('Your Calender is Ready\n')

        for i in range(0, 6 + 1):
            print(day[i], end=' ')              # print day's for calender
        print()
        for i in range(row):

            for j in range(column):

                if values <= days[m - 1]:        # while d0 is less than j
                    if i == 0 and j < d0:        # it will print blank space
                        stack.push(' ')          # use push() to add blanks
                        continue

                    stack.push(values)           # add days using push() method
                    values += 1

        for i in range(stack.size()):
            stack_element = stack.pop()         # pop element from stack and store in local variable
            stack1.push(stack_element)          # again push element into stack for reverse

        for i in range(row):

            for j in range(column):
                if stack1.size() > 0:
                    x = stack1.pop()          # access element one by one using pop() method
                    x1 = str(x).ljust(2)       # ljust() method to print in calender structure
                    print(x1, end=" ")

            print()

    def anagram_stack(self):
        """
        This method is used to print prime anagram in reverse order.
        """
        for i in utility.get_anagram_prime():  # get anagram numbers which are prime
            stack.push(i)  # push numbers into stack

        for i in range(0, stack.size()):
            print(stack.pop())  # print in reverse order

    def anagram_queue(self):
        """
        This method is used to print prime anagram using queue.
        """

        for i in utility.get_anagram_prime():  # get anagram numbers which are prime
            queue.enqueue(i)  # add numbers into queue

        for i in range(0, queue.size()):
            print(queue.dequeue())

    def prime_number_2d_array(self):
        """
        This method is used to store prime number in matrix or 2d array
        and print in proper order.
        """

        prime_list = utility.get_prime()  # get prime number
        row = 10
        column = 25
        limit = 100
        # create empty 2d array
        two_d_array = [[0 for j in range(column)] for i in range(row)]

        k = 0
        for i in range(row):

            for j in range(column):

                if k < len(prime_list):
                    if prime_list[k] <= limit:  # prime number check with the limit
                        two_d_array[i][j] = prime_list[k]  # add number into array
                        k += 1

            limit += 100  # increment limit by 100 for each iteration

        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")  # display elements in 2d array format

            print()

    def anagram_2d_array(self):
        """
        This method is used to store prime anagram and prime number which are not anagram in matrix or 2d array.
        and print them accordingly
        """
        prime_list = utility.get_prime()  # get prime numbers
        anagram_list = utility.get_anagram_prime()  # get anagram numbers which is prime also
        not_anagram = []
        row = 10
        column = 25

        two_d_array = [[0 for j in range(column)] for i in range(row)]
        k = 0
        index = 0
        for i in prime_list:
            if anagram_list.__contains__(i) is not True:  # if file not contains same element
                not_anagram.append(i)  # append into not_anagram list

        for i in range(row):

            for j in range(column):

                if k < len(anagram_list):
                    two_d_array[i][j] = anagram_list[k]  # add element of anagram list into array
                    k += 1

                if k >= len(anagram_list) and index < len(not_anagram):
                    two_d_array[i][j] = not_anagram[index]  # add element of not_anagram list
                    k += 1  # into same array after anagram_list
                    index += 1
        for i in range(row):

            for j in range(column):

                if two_d_array[i][j] != 0:
                    print(two_d_array[i][j], end=" ")  # print 2d array

            print()


# --------------------------------------------------------------------------------------------------------------------

class BinarySearchTree:
    """
        This class is used to count the binary trees
    """

    def count(self, number_of_items_chosen):  # Method to count the number of binary trees

        n = number_of_items_chosen

        number = int((math.factorial(2 * n)) / (math.factorial(n + 1) * math.factorial(n)))

        print(number)

# ----------------------------------------------------- END -------------------------------------------------------

