from ds.utilities.utility import Methods


def anagram_runner():
    """
     THIS METHOD IS USED TO PRINT PRIME ANAGRAM BETWEEN 0-1000
     IN REVERSE ORDER IN A STACK
    """
    logic_obj = Methods()           # creating the object of method class
    logic_obj.anagram_stack()       # function call


if __name__ == "__main__":          # calling the method inside the main method
    anagram_runner()
