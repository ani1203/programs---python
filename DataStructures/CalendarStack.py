from ds.utilities.utility import Methods


def calender_stack_runner():
    """
    THIS METHOD IS USED TO RUN THE CALENDAR
    """

    logic_obj = Methods()                    # creating object of the method class

    try:
        month = int(input('Enter Month'))      # enter the month number
    except Exception as e:
        print(e)
        print("Enter integer only ")
    try:
        year = int(input('Enter Year'))         # enter the year
    except Exception as e:
        print(e)
        print("Enter integer only")

    logic_obj.calender_stack(month, year)


if __name__ == "__main__":
    calender_stack_runner()                 # calling the method inside the main method
