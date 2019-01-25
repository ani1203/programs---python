# @author - anil mehta
# version 3.7
# since - 5th january 2019

import re


class ReplaceString:
    """
    this method is created to Replace <<name>> by first name of the user ( assume you are the user)
    replace <<full name>> by user full name.
    replace any occurance of mobile number that should be in format 91-xxxxxxxxxx by your contact number.
    replace any date in the format XX/XX/XXXX by current date in the following string

    """
    @staticmethod    # making the method static
    def regex():
        # assigning the sentence in which the changes are to be done to a variable
        string = '\nHello <<name>>, We have your full name as <<full name>> in our system.' \
                 '\nYour contact number is 91-xxxxxxxxxx.' \
                 '\nPlease, let us know in case of any clarification Thank you BridgeLabz 01/01/2019. '

        # creating a list for strings that needs to be replaced by user input

        template = ['<<name>>', '<<full name>>', 'xxxxxxxxxx', '01/01/2019']
        print()

        # creating another list of uer input that will replace the strings mentioned above
        # list will take all the user input
        list_ = ['Enter Your First Name: ', 'Enter Your Full Name: ', 'Enter Your Mobile Number(10 digits only):',
                 "Enter Today's Date[dd/mm/yyy]:"]

        for i in range(4):     # creating for loop for replacing the strings using random expression module
            print(list_[i])     # printing above list element by element in a loop so as to take user input
            # using random expression method to replace strings in sentence by given input
            replaced_string = re.sub(template[i], str(input()), string)
            # assigning the replaced_string to string again
            string = replaced_string

        return string    # string will print the sentence with all the changes


if __name__ == "__main__":  # creating the main method to execute the functioning  method
    try:                            # using exceptions to give validation
        # creating the object of ReplaceString class
        obj = ReplaceString()
        print("The Modified String with user information are as follows")
        print(obj.regex())     # using the object of class to call the functioning method
    except Exception as e:
        print(e)
