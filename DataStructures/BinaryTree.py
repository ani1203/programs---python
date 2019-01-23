from ds.utilities.utility import BinarySearchTree


def binary_search_tree():

    binary_tree = BinarySearchTree()  # creating the object of the BinarySearchTree class

    try:

        number_of_nodes = int(input("Enter the Number of Nodes:\n"))  # entering the number of nodes present

    except ValueError:

        print("Enter integer value")

    except TypeError:                          # giving exception for validation

        print("enter valid data")

    binary_tree.count(number_of_nodes)  # number of possible of tree formation


if __name__ == "__main__":

    binary_search_tree()
