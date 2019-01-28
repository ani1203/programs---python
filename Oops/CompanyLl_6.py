import json
from ds.utilities.utility import LinkedList

l1 = LinkedList()  # creating object of LinkedList class to access all the method present in that class
company_info = json.load(open("company.json", "r"))  # opening and reading the 'company' JSON file and
# converting it to the python Dictionary storing in a variable


# 'add_companies' function adds each companies detail to the LinkedList node
def add_companies():
    global name, logo
    # show_symbols()
    name = input("enter the company name")
    logo = input("enter the symbol for the company")
    for val in company_info:  # traversing the dictionary
        l1.append(company_info[val])  # inserting each company details to the LinkedList
    print("\nCompanies detail successfully added to the LinkedList\n")


# 'show_symbols' function displays company name and their symbol for the user reference
def show_symbols():
    for val in company_info:  # traversing through the dictionary
        print(company_info[val]["company_name"], "== ", company_info[val]["company_symbol"])
    print()


# this function delete the node of the LinkedList containing particular company details after getting company symbol
# input from the user
def del_companies():
    show_symbols()  # calling show_symbols function to display symbols
    try:
        symbol = input("Enter the Symbol of companies: ")
        for val in company_info:  # traversing through the Dictionary to delete the user-input company details
            if symbol == company_info[val]["company_symbol"]:
                l1.remove(company_info[val])  # deleting the particular company detail from the LinkedList
                print("\nCompany details successfully deleted from the LinkedList\n")

    except Exception as e:  # handling the exception
        print(e)


# 'CompanyShare' as Main class
class CompanyShare:
    while True:
        # displaying main menu
        print("enter 1 To delete company to LinkedList")
        print("enter 2 To add company from LinkedList")
        print("enter 3 For Exit")

        global choice
        try:
            choice = int(input("\nEnter your choice: "))
        except Exception as e:
            print(e)
            print("enter the valid value")
        try:
            if choice == 1:
                del_companies()  # calling method to add company details
            elif choice == 2:
                add_companies()  # calling method to delete particular company detail
            elif choice == 3:
                print("exit")
                exit(0)  # terminating the program
            else:
                print("Invalid choice !!! Please Try again")
        except Exception as e:  # handling the exception
            print(e, "\n!!! Invalid Input !!!\n")


# from this python file only program will compile not from the imported file(s)
if __name__ == '__main__':
    s1 = CompanyShare()  # creating object of 'CompanyShare'
