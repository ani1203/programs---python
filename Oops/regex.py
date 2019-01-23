import re


class RegularExpression:

    @staticmethod
    def regex():

        string = '\nHello <<name>>, We have your full name as <<full name>> in our system.' \
                 '\nYour contact number is 91-xxxxxxxxxx.' \
                 '\nPlease, let us know in case of any clarification Thank you BridgeLabz 01/01/2019. '

        template = ['<<name>>', '<<full name>>', 'xxxxxxxxxx', '01/01/2019']
        print()

        list_ = ['Enter Your First Name: ', 'Enter Your Full Name: ', 'Enter Your Mobile Number(10 digits only):',
                 "Enter Today's Date[dd/mm/yyy]:"]

        for i in range(4):
            print(list_[i])
            replaced_string = re.sub(template[i], str(input()), string)
            string = replaced_string

        return string


def re_runner():
    try:
        obj = RegularExpression()
        print("The Modified String with user information are as follows")
        print(obj.regex())
    except Exception as e:
        print(e)


if __name__ == "__main__":
    re_runner()
