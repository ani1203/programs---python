# @author - anil mehta
# version 3.7
# since - 5th january 2019


class Stock:
    """
    this method is created to  to read in Stock Names, Number of Share, Share Price and
    Print a Stock Report with total value of each Stock and the total value of Stock.

    """

    @staticmethod         # making the method static
    def stock_report():
        total_stock = None
        share_price = None          # putting values as None to avoid minute error
        number_of_share = None
        try:                          # giving exception for validation
            total_stock = int(input("enter the total number of stock\n"))  # entering the total stocks
        except ValueError:
            print("enter only integer value")       # giving exception for validation

        # using 'for' loop to print as many stocks and its report that the user is giving

        for i in range(0, total_stock):
            stock_name = input("enter the stock name\n")
            try:                        # giving exception for validation
                number_of_share = int(input("enter the number of share\n"))  # entering the number of share
            except Exception as e:
                print(e)
            try:                            # giving exception for validation
                share_price = int(input("enter the share price\n"))  # entering the share price
            except Exception as e:
                print(e)                    # giving exception for validation
                print("enter only integer values")

            print("value of each share ", "==>", share_price)
            total_value = number_of_share*share_price
            print("total value of ", stock_name, "  ==>", str(total_value))


if __name__ == '__main__':    # creating a main method and calling the functioning method inside main method
    try:                            # giving exception for validation
        object_1 = Stock()      # creating object of Stock class
        object_1.stock_report()
        # calling method using object of class
    except Exception as e:
        print(e)
        print("enter valid values")
