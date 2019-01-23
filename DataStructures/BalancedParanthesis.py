from ds.utilities.utility import Stack


def balance_parentheses():
    """
    THIS METHOD DISPLAYS WHETHER PARENTHESES ARE BALANCED OR NOT
    """
    stack = Stack()                  # creating the object of stack class
    try:
        string = input("Enter Expression to check for balanced Parentheses: ")
    except Exception as e:
        print(e)                    # giving exceptions for validation
        print("Enter String")

    stack.balanced_parentheses(string)  # function call


if __name__ == "__main__":
    balance_parentheses()              # calling the method inside the main method
