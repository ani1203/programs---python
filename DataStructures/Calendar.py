from ds.utilities.utility import Methods


def calendar_runner():
    """
    THIS METHOD DISPLAYS THE CALENDAR
    """

    logic_obj = Methods()  # creating object of the method class

    try:
        month = int(input('Enter month: '))  # enter the month number
    except ValueError:
        print("Enter integer only ")

    try:
        year = int(input("Enter Year: "))  # enter year
    except ValueError:
        print("Enter integer only")
    logic_obj.calendar(month, year)


if __name__ == "__main__":
    calendar_runner()           # calling the method inside the main method
