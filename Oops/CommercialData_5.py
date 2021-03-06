from Oops.Methods import *


# 'StockAccount' class contains main menu
class StockAccount:
    data = DetailData()  # creating object of 'DetailData' class to access all the functionality of the class
    while True:
        # displaying main menu
        print("\n-----------Stock Accounts-----------")
        print("enter 1.To add a Customer")
        print("enter 2.To add a Company")
        print("enter 3.To display Customer")
        print("enter 4.To display Company")
        print("enter 5.For Transaction")
        print("enter 6.For Exit")

        global choice
        try:
            choice = int(input("\nEnter your choice: "))
        except Exception as e:  # handling the exception for bad input
            print(e, "\n!!! Invalid Input !!!\n")
        try:
            if choice == 1:
                data.add_customer()  # calling 'add_customer' method from 'DetailData' class through reference variable
            elif choice == 2:
                data.add_company()  # calling 'add_company' method from 'DetailData' class through reference variable
            elif choice == 3:
                print("\n---------Details of all Customers--------")
                data.display_customer()  # calling 'display_customer' method from 'DetailData' class through reference
                # variable
            elif choice == 4:
                print("\n---------Details of all Companies--------")
                data.display_company()  # calling 'display_company' method from 'DetailData' class through reference
                # variable
            elif choice == 5:
                data.transaction()  # calling 'transaction' method from 'DetailData' class through reference variable
            elif choice == 6:
                print("\nClosing....\nClosed Successfully.")
                exit(0)  # terminating the program
            else:
                print("Invalid choice !!! Please Try again")
        except Exception as e:  # handling exception for bad input
            print(e, "\n!!! Invalid Input !!!\n")


# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    s1 = StockAccount()
