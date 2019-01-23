import json


class Inventory:

    @staticmethod
    def food_items():
        file = open("inventory_items.json", "r")
        file_read = file.read()
        file.close()
        file_items = json.loads(file_read)
        # print(file_items, "\n")
        print("which item you want to buy")
        print(" enter 0 for rice", "\n", "enter 1 for wheat", "\n", "enter 2 for pulses","\n")
        choice = int(input("enter your choice\n"))
        if choice == 0:
            print("total price for all the different kinds of rice are")
            for rice in file_items["rice"]:
                rice_total = int(rice["price"]) * int(rice["weight"])
                print(rice["name"], "=", rice_total)

        # print("\n")
        if choice == 1:
            print("total price for all the different kinds of wheat are")
            for wheat in file_items["wheat"]:
                wheat_total = int(wheat["price"]) * int(wheat["weight"])
                print(wheat["name"], "=", wheat_total)

        # print("\n")
        if choice == 2:
            print("total price for all the different kinds of pulses are")
            for pulse in file_items["pulse"]:
                pulse_total = int(pulse["price"]) * int(pulse["weight"])
                print(pulse["name"], "=", pulse_total)


if __name__ == '__main__':
    Inventory.food_items()
