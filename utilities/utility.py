import random
import math
import time

# @author - anil mehta
# version 3.7
# since - 5th january 2019


# all the methods will be created here and it will be called in the main file of that particular program...

# **************************************starts****************************************************************

# 1st program
# replacing the "username" in the sentence with the input name "


def replace(s1):
    sentence = "hello username , how are you ?"
    if len(s1) >= 3:                                    # minimum length should be 3
        print(sentence.replace("username", s1))         # using function to replace the particular word
    else:
        print("enter the valid name")

# =================================================              ======================================================

# 2nd program
# method to check weather a given number is a leap year or not


def leap_year(year):
    if year > 999:                               # enter year that is a 4 digit number
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            print("year is a leap year")         #
        else:
            print("enter a valid year")

# =================================================              ======================================================


def is_leap(year):
    """Checks if year is a leap year"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# =====================================================   ============================================================


# 3rd program
# method to check no. of heads and tails based on no. of flips


def flip_coin(flip):
    tail = 0
    head = 0
    for i in range(flip):
        rdm = random.randint(0, 1)   # using random function to generate number in range

        if rdm < 0.5:                # using that random number to increment head and tail
            head += 1

        else:
            tail += 1
    print("percentage of head =", ((head / flip) * 100))
    print("percentage of tails =", ((tail / flip) * 100))


# =================================================              ======================================================

# 4th program
# printing the power table of 2 by giving value of N as input


def power_table(N):
    real_number = 2
    if (N >= 0) and (N < 31):      # N value should be within the given range
        for i in range(N):         # use loop to print the power table of 2
            print(real_number)
            real_number *= 2
    else:
        print("enter the valid value of N")


# =================================================              ======================================================

# 5th program
# program to find out the Nth harmonic number

def harmonic(n):
    number = 0
    if n != 0:
        for i in range(1, n+1):
            number = number + (1/i)     # number should be in loop to print number with different i value
        print(number)
    else:
        print("enter a valid value")

# =================================================              ======================================================

# 6th program
# program to find out the factors of number N


def factor_prime(n):
    print("prime factors of", n, "are")
    for i in range(2, n):
        while n % i == 0:       # till modulus is not equal to zero loop goes on
            n = n/i
            print(i)
    if n >= i:                  # if somehow number become greater than zero then print value(n)
        print(n)

# =================================================              ======================================================

# 7th program
# Print Number of Wins and Percentage of Win and Loss o f a gambler


def gamble(stake, goal, time_1):
    n = random.randint(0, 1)                 # generate random numbers b/w range using random function
    win = 0
    bet = 0
    loss = 0
    for i in range(0, time_1):
        cash = stake
        while (cash != goal) and (cash != 0):  # gambler will play until he reaches his goal or gets blank
            bet += 1                            # each time he wil place a bet until he reaches his goal
            if n < 0.5:
                cash += 1
            else:
                cash -= 1
            if cash == goal:                    # gambler wins if he reaches its goal else loose
                win += 1
            else:
                loss += 1
    print("total no. of wins =", win)
    print("total no. of loss =", loss)
    print("percentage of win =", (win / (win + loss)) * 100)
    print("percentage of loss =", (loss / (win + loss)) * 100)

# =================================================              ======================================================

# program to check weather any given number is a prime number or not


def check_prime(n):
    count = 0
    for i in range(2, (n-1)):       # 1 and number itself should not be included because that applies for every number
        if n % i == 0:
            count += 1              # count increases  for every i dividing n

    if count == 0:
        print("number is a prime number")
    else:
        print("number is not a prime number")


# =================================================              ======================================================

# 8th program
# program for windchill

def windchill(t, v):
    s = v**0.16
    if (t < 50) and (v > 3) and (v < 120):          # all three conditions should be true
        w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*s
    else:
        print("enter the valid value")
    print("the effective temperature ( wind chill) =", w)

# =================================================              ======================================================


# 9th program
# program to find the roots of the quadratic equation

def roots(a, b, c):
    delta = (b * b) - (4 * a * c)
    root1 = ((-b) + math.sqrt(delta)) / (2 * a)  # sqrt is the square root function imported from math module
    root2 = ((-b) - math.sqrt(delta)) / (2 * a)
    print("value of 1st root =", root1)
    print("value of 2nd root =", root2)

# =================================================              ======================================================


# 10th program
# program to find out sum of three triplets is equal to zero or not

def triplets():
    list_size = int(input("enter the list size\n"))
    a = []
    print("enter the elements")
    for i in range(0, list_size):
        a.append(eval(input()))
    count = 0
    for l in range(0, list_size):           # every next number should be 1 more than the previous number in the loop
        for j in range(l+1, list_size):
            for k in range(j+1, list_size):
                if a[l]+a[j]+a[k] == 0:        # validating sum of triplets is 0 or not
                    print(a[l], a[j], a[k])
                    count += 1                 # count increases for every triplet

    print("total no. of triplets =", count)

# =================================================              ======================================================


# 11th program
# program for using stopwatch , and to check the elapsed time..

def start1():
        start1.start = time.time()      # start method for stopwatch


def stop1():
        stop1.stop = time.time()        # stop method for stopwatch


def elapsed_time():
    elapsed_time = stop1.stop - start1.start    # elapsed time for stopwatch
    print("elapsed time =", elapsed_time)


# =================================================              ======================================================


# 12th program
# program to find out the euclidean distance from the origin i.e (0, 0)..


def distance_origin(x, y):
    distance = math.sqrt(x**2 + y**2)                   # square root function used from math module
    print("euclidean distance from the origin to (x, y) =", distance)

# =================================================              ======================================================


# 13th program
# program to print the two dimensional list


def list_2d(a, rows, col):
    print("enter the elements of the list")
    for i in range(rows):
        for j in range(col):        # loop for creating the list elements during run time
            a[i][j] = int(input())
    for i in range(rows):
        for j in range(col):
            print(a[i][j], end="  ")  # loop for printing the  2d-list
        print()


# =================================================              ======================================================


# 14th program
# program to convert temperature from  fahrenheit to celsius and vice versa


def conversion():
    c = 0
    f = 0
    n = int(input("enter the value of n \n"))
    if n == 0:
        f = float(input("enter temperature in fahrenheit\n"))   # loop to convert from fahrenheit to celsius
        print("temperature in celsius is ")
        celsius = (f - 32) * (5 / 9)
        print(celsius)
    if n == 1:
        c = float(input("enter temperature in celsius\n"))
        print("temperature in fahrenheit")                      # loop to convert from celsius to fahrenheit
        fahrenheit = (c * 9 / 5) + 32
        print(fahrenheit)


# =================================================              ======================================================


#                   ----------------method to check if a number is a prime or not ------------------


def prime_check(n):
    i = 2
    while i < n/2:
        if n % i == 0:
            return False
        i += 1

        return True

# =================================================              ======================================================


def get_prime():
    list = []
    is_prime = True
    for i in range(1001):
        if i == 0 or i == 1:
            continue
        is_prime = True
        for j in range(2, i):
            if i%j == 0:
                is_prime = False
        if is_prime:
            list.append(i)
    return list
# =======================================================    ======================================================


def get_anagram_prime():
    x = get_prime()
    x = [str(i) for i in x]
    anagram = []
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if sorted(x[i]) == sorted(x[j]):
                anagram.append((x[i]))
                anagram.append(x[j])
    return anagram

# ==================================================        ==========================================================
# 15th program
# program monthly payments you would have to make over Y years to pay off a P principal loan amount at R per cent


def month_pay(P, Y, R):                 # p = principal amount
    r = R/(12*100)                      # r = rate of interest
    n = 12*Y                             # y = years
    payment = (P*r)/(1-(1+r)**(-n))
    print(payment)


# =================================================              ======================================================


# 16th program
# program to print prime number between 0 to 1000


def prime_num():
    for i in range(1, 1001):
        temp = 0                           # define a temporary variable outside
        for j in range(2, i-1):            # based on temporary variable value
            if i % j == 0:
                temp += 1

        if temp == 0:                       # if value does not increment , then its a prime no.
            print(i, end=" ")


# =================================================              ======================================================


# 17th program
# program to print the day of the week that date falls on


def day_week(m, d, y):
    list1 = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2          # formulas given in the question
    d0 = (d + x + 31*m0 // 12) % 7              # this formula will generate values b/w 0 to 6
    print(list1[d0])                            # printing the list


# =================================================              ======================================================


# 18th program
# note vending machine

def note_machine(rupees):
    a = [1000, 500, 100, 50, 10, 5, 2, 1]       # create a list of notes in ascending orders
    note = 0
    for i in range(0, len(a)):
        if rupees // a[i] > 0:
            print("no. of notes of ", a[i], " is ", rupees // a[i])  # remainder will give no. of notes
            note = note + (rupees // a[i])
            rupees = rupees % a[i]                              # quotient will give next value of rupee
    print("no. of notes are " + str(note))


# =================================================              ======================================================


# 19th program
# anagram detection program


def check_anagram():
    temp = 0
    str1 = input("enter the 1st string\n")
    str2 = input("enter the second string\n")
    str3 = str1.upper()                         # convert both the string to upper case for equality
    str4 = str2.upper()
    if len(str1) == len(str2):                  # check if length is equal or not , then only proceed
        for i in range(0, len(str3)):
            for j in range(0, len(str4)):       # outer loop will compare the value of first string to second
                if str3[i] == str4[j]:
                    temp += 1
                    break                # length of string should be equal to value of temp , then only its anagram
        if len(str1) == temp:
            print(str1, "is a anagram of ", str2)
        else:
            print(str1, "is not a anagram of ", str2)
    else:
        print("not an anagram")


# =================================================              ======================================================


# 20th program
# program to compute the square root of a non-negative number


def sqt_negative(c):
    epsilon = 1e-15
    t = c                   # giving value of c to another variable t
    print("square root of the non-negative number ", c, "=")
    if c > 0:
        while abs((t - c / t)) > epsilon * t:     # using the formula given in the question inside loop
            t = (c / t + t) / 2                    # using the condition given in the question only
    print(t)


# =================================================              ======================================================


# 21st program
# program to bubble sort a list


def bubble(arr):
    for c in range(1, len(arr)):            # create a temporary list for assigning values
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                temp = arr[i]               # in this loop values are exchange if loop condition satisfied
                arr[i] = arr[i+1]           # assigning (i+1) to (i)
                arr[i + 1] = temp           # assigning value of temp to (i +1)

    print(arr)


# =================================================              ======================================================


# 22nd program
# insertion sort


def insert(a):
    for j in range(1, len(a)):       # taking range from index no. 1 onwards
        temp = a[j]                   # for comparison of all the other numbers with 0 index number element
        k = j                        # assigning value of j to another variable j
        while k > 0 and a[k - 1] > temp:
            a[k] = a[k - 1]           # if the loop satisfies and values will be exchanged
            k -= 1                    # at the same time k will decrement till loop condition is not true
        a[k] = temp                   # finally assigning the temp elements to list

    print(a)


# =================================================              ======================================================


# 23rd program
# Python program for implementation of MergeSort


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2             # Finding the mid of the array
        L = arr[:mid]                   # creating two temp variables
        R = arr[mid:]                   # for left half and the right half

        mergeSort(L)                    # Sorting the first half
        mergeSort(R)                        # Sorting the second half

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]               # here left array elements will be assigned to original array
                i += 1
            else:
                arr[k] = R[j]               # here right array elements will be assigned to original array
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1                          # again checking if any element is left or not

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# =================================================              ======================================================


# 24th program
# converting a decimal into binary numbers


def to_binary(number):
    result = ""
    while number != 0:
        remainder = number % 2                   # gives the exact remainder
        number = number // 2                    # quotient will be again used as a number
        result = str(remainder) + result
    print("The binary representation is", result)


# =================================================              ======================================================


# 25th program
# nibble program


def to_decimal(number):
    while len(str(number)) < 8:
        number = number + str(0)

    s3 = number[4:8]
    s4 = number[0:4]
    swap = s3 + s4
    b = str(swap)
    print(b)


# =================================================              ======================================================


# 26th program
# program to generate a random coupon number


def coupons(list1):
    cnt = 0                                      # starting the count resulting from the loop
    while len(list1) > 0:
        x = random.randint(0, 9)                # generate number between 0-9 using random function
        cnt += 1                                 # increment cnt
        if x in list1:                              # check x is present in list or not
            list1.remove(x)                          # if matched then remove that
        print(x)
    print("Total random number needed to have all distinct numbers:", cnt)

# =================================================              ======================================================


# 27th program
# program for different sorting methods for integers and strings

# I. ------------------------------------Binary Search Integer------------------------------------------------------

def BinaySearchInteger(n):
    start1()                           # start method to start the timer
    flag = 1
    print("Enter the array elements")
    arr = [int(input()) for i in range(n)]  # input the list elements during the run time
    x = len(arr)
    key = int(input("Enter the Key to search"))
    start = 0
    end = x - 1
    arr.sort()                              # sort function to sort the list
    print("Sorted Array", arr)
    while start <= end:
        mid = (start + end) // 2         # will give the middle value
        if key == arr[mid]:
            flag = 0
            print("Element is found at the location", mid)
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if flag == 1:
        print("Element Not Found")
        stop1()                           # stop method to stop the timer for checking method run time
        elapsed_time()                    # function to check the elapsed time of method


# II. -----------------------------------------Binary Search String---------------------------------------------------

def BinaySearchString(n):
    start1()                                         # start method to start the timer for checking method run time
    flag = 1
    print("Enter the String array elements")
    arr = [(input()) for i in range(n)]
    x = len(arr)
    key = (input("Enter the Key to search"))          # enter the element you want to search
    start = 0
    end = x - 1                                        # sort function to sort the list
    arr.sort()
    print("Sorted Array", arr)
    while start <= end:
        mid = (start + end) // 2
        if key == arr[mid]:
            flag = 0
            print("Element is found at the location", mid)
        if key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    if flag == 1:
        print("Element Not Found")
    stop1()                            # stop method to stop the timer for checking method run time
    elapsed_time()                   # function to check the elapsed time of method


# -------------------------------- III. Insertion Sort for Integer --------------------------------------------

def InsertionSortInteger(n):
    start1()                                    # start method to start the timer for checking method run time
    print("Enter the Elements in the array")
    arr = [int(input()) for i in range(n)]
    x = len(arr)
    for i in range(1, n):
        j = i
        temp = arr[i]
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp
    print("Sorting Elements are")
    for i in range(0, n):
        print(arr[i])
    stop1()                               # stop method to stop the timer for checking method run time
    elapsed_time()                        # function to check the elapsed time of method


# --------------------------------------------IV Insertion Sort for String-------------------------------------------

def InsertionSortString(n):
    start1()                                    # start function to start the timer
    print("Enter the Elements in the array")
    arr = [(input()) for i in range(n)]         # creating a string list by giving input
    # x=len(arr)
    for i in range(1, n):
        j = i
        temp = arr[i]
        while j > 0 and temp < arr[j - 1]:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = temp
    print("Sorting Elements are")
    for i in range(0, n):
        print(arr[i])
    stop1()                                    # stop function to stop the timer
    elapsed_time()                             # to calculate the elapsed time


# V -----------------------------------------Bubble Sort for Integer----------------------------------------
def BubbleSortInteger(n):
    start1()                                        # start function to start the timer
    print("Enter the Elements in the array")        # creating the integer list
    arr = [int(input()) for i in range(n)]
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print("Sorted Array is")
    for i in range(0, n):
        print(arr[i])
    stop1()                                              # stop function to stop the timer
    elapsed_time()                                   # to calculate the elapsed time


# V ------------------------------Bubble Sort for String---------------------------------------------------------

def BubbleSortString(n):
    start1()                                                # start function to start the timer
    print("Enter the String Elements in the array")
    arr = [(input()) for i in range(n)]                     # creating the string list for bubble sort
    for i in range(0, n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print("Sorted Array is")
    for i in range(0, n):
        print(arr[i])
    stop1()                                                        # stop function to stop the timer
    elapsed_time()                                               # to calculate the elapsed time

# =================================================              ======================================================


# 28th program
# program to check a number is a palindrome or not


def palindrome(n):
    a = []
    n1 = str(n)                                        # converting number to string
    s = n1[::-1]                                         # reversing the number
    if s == n1:
        a.append(s)                                          # inserting the value into list
        print("given no. is palindrome of ", a)
    else:
        print("number is not a palindrome")
    print(a)


# =================================================              ======================================================


# 29th program
# program to guess the number that the user is thinking ....


def number(first, last):
    res = last - first
    if res == 1:                                         # loop will return the first number if difference is 1
        return first
    mid = first + (last - first)/2                              # finding the mid value for further process
    print("is the number less than ", mid, "if yes press 1 else press 0")
    n = int(input())
    if n == 1:                                   # pressing 1 means yes and pressing 0 means switching to next condition
        return number(first, mid)
    elif n == 0:
        return number(mid, last)
    else:
        print("enter the valid value")


# =================================================              ======================================================


# 30th program
# program to binary search a word from the word list


def file():
    print("input the string you want to search")
    name = input()                                  # enter the string you want to search from the text file
    f = open("test1.txt", "r").readline()           # this function will open the txt file and read it

    if name in f:                                   # if the required str4ing is present inside loop satisfies
        print("string is present")                  # or the string is not present
    else:
        print("string is not present")

# =================================================              ======================================================


# 31st program
# permutation of a string


def permute(a, l, r):
    if l == r:                   # checking whether string is of single character or not
        print(''.join(a))        # then printing the given string as it is
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)      # recursion of the function
            a[l], a[i] = a[i], a[l]  # swap back, for the next loop


# **************************************     end   ****************************************************************
