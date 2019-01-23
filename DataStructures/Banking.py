from ds.utilities.utility import Queue


def cash_counter():
    """
    METHOD TO DEPOSIT OR WITHDRAW MONEY FROM BANK
    """

    queue = Queue()             # creating the object of Queue class
    bank_cash = 1000
    try:
        no_of_people = int(input('Enter Number of People in the Queue:'))     # number of people standing in bank
    except Exception as e:
        print(e)
        print("Enter no of people in integer only:")
    for i in range(0, no_of_people):
        queue.enqueue(i)                             # adding the number of people present

    print('Welcome To the Bank')
    for i in range(0, queue.size()):
        print('1.Deposit cash \n 2.Withdraw cash \n')       # entering the choice to withdraw or deposit
        choice = int(input("Enter choice:"))

        if choice == 1:

            try:
                deposit_amount = int(input("Enter Deposit Amount: "))  # enter the amount to be deposited
            except Exception as e:
                print(e)
                print("Enter amount in integer only..")
            bank_cash = bank_cash + deposit_amount
            queue.dequeue()

        if choice == 2:
            print()
            try:
                withdraw_amount = int(input("Enter How much cash you want to Withdraw:")) # enter amount to be withdrawn
            except Exception as e:
                print(e)
                print("Enter withdraw amount in integer only...")
            if withdraw_amount < bank_cash:             # checking the withdrawn amount is more or less than the cash
                bank_cash = bank_cash - withdraw_amount
                queue.dequeue()

            if withdraw_amount > bank_cash:         # output will be generated accordingly
                print('Insufficient Fund in Bank')
                print('1. Kindly enter cash within ' + str(bank_cash) + ' range  \n 2.If you do not want and leave')
                withdraw_choice = int(input("Enter choice:"))

                if withdraw_choice == 1:
                    try:
                        withdraw_amount = int(input('Enter Withdraw Amount:'))
                    except Exception as e:                                        # giving exceptions for validation
                        print(e)
                        print("Enter withdraw amount in integer only")
                    if withdraw_amount <= bank_cash:
                        bank_cash = bank_cash - withdraw_amount
                    queue.dequeue()

                if withdraw_choice == 2:
                    queue.dequeue()

        if i < queue.size():
            print('Next Person')

    print('Bank Balance => ' + str(bank_cash))


if __name__ == "__main__":
    cash_counter()                  # calling the method inside the main method

