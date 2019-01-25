# @author - anil mehta
# version 3.7
# since - 5th january 2019

import json


class StockReport:
    @staticmethod
    def stock():
        with open('stock.json', 'r') as file:
            file_content = file.read()  # this function is used to read json file
            file.close()                # closing the file
        main_file = json.loads(file_content)  # using loads() convert json data into python data
        count = 0
        for element in range(len(main_file['stock'])):  # loop iterate till last element fo stock
            temp = 1
            for key in (main_file['stock'][element]):

                if element == 0 and count == 0:
                    for key1 in (main_file['stock'][0]):
                        print(key1, end='      ')  # print keys element of json
                        count += 1
                        if count == len(main_file['stock'][0]):
                            print(' Total Price ', end=' ')  # print total price at end

                    print()

                print(main_file['stock'][element][key], end='\t\t\t\t')  # print company names
                if temp == len(main_file['stock'][element]):
                    # print data of stock report
                    print(
                        main_file['stock'][element]['total share'] * main_file['stock'][element]['share price'],
                        end='\t\t\t')
                temp += 1  # increment counter by 1
            print()


if __name__ == '__main__':
    StockReport.stock()



