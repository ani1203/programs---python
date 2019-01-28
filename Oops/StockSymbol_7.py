
import json
from ds.utilities.utility import Stack

s1 = Stack()  # creating object of Stack class to access all the method present in that class
content = json.load(open("transaction.json", "r"))  # opening and reading the 'company' JSON file and
# converting it to the python Dictionary storing in a variable


# this function push the symbol of the companies to the created Stack
def push_1():
    # global name, logo
    # show_symbols()
    # name = input("enter company name")
    # logo = input("enter the symbol")
    for val in range(len(content['transaction'])):  # traversing through the Dictionary
        type = str(content['transaction'][val]["buy_sell"])  # converting type of transaction to string for
        # concatenation
        s1.push(content['transaction'][val]["company_symbol"] + " - " + type)  # concatenating company symbol and the
        # type of transaction done and pushing it to the Stack
    print("\nCompanies symbol added to the Stack\n")


# def show_symbols():
#  for val in content:  # traversing through the dictionary
#       print(content[val]["customer_name"], "== ", content[val]["company_symbol"])
#  print()


# this method pop out the element from the Stack
def pop_1():
    # show_symbols()
    global logo
    logo = input("enter the symbol")
    removed = s1.pop()  # popping the element
    print("\n'", removed, "' deleted from the Stack\n")


# 'Symbol' as Main class
class Symbol:
    while True:
        # displaying main menu
        print("enter 1.To delete company symbols to Stack")
        print("enter 2.To add company symbols from Stack")
        print("enter 3.For Exit")

        global choice
        try:
            choice = int(input("\nEnter your choice: "))
        except Exception as e:  # handling the exception for user-input
            print(e, "\n!!! Invalid Input !!!\n")
        try:
            if choice == 1:
                pop_1()  # calling 'push_symbols' function
            elif choice == 2:
                push_1()  # calling 'pop_symbol' function
            elif choice == 3:
                print("exited")
                exit(0)  # terminating the program
            else:
                print("Invalid choice !!! Please Try again")
        except Exception as e:
            print(e, "\n!!! Invalid Input !!!\n")


# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    s1 = Symbol()  # creating object of 'Symbol'
