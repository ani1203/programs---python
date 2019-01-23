from ds.utilities.utility import Deque


def is_palindrome(word):
    """
    THIS METHOD IS USED TO CHECK WHETHER THE GIVEN INPUT
     IS A PALINDROME OR NOT
    """
    queue = Deque()              # creating object of Deque class

    for ch in word:
        queue.insert_rear(ch)    # adds all the characters from back

    is_equal = True

    while queue.size() > 1 and is_equal:
        first = queue.remove_front()     # removes the characters from the front of the queue
        last = queue.remove_rear()      # removes the characters from the rear of the queue
        if first != last:
            is_equal = False

    return is_equal


if __name__ == '__main__':
    word = input("enter the word\n")        # enter the word to check its palindrome or not
    print(is_palindrome(word))              # printing and calling the method inside the main method



