"""
Exercises from Chapter 1 - Python Premier
"""
import random

""" 1.1 : Write a short Python function, is_multiple(n, m), that takes two integer values and returns True if n is a
multiple of m, that is, n = mi for some integer i, and False otherwise. """


def is_multiple(n, m):
    """ checks if n is a factor of m """
    if m % n == 0:
        return True
    else:
        return False


""" 1.2 : Write a short Python function, is_even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators. """


def is_even(k):
    x = '{0:08b}'.format(k)
    """
    Just to explain the parts of the formatting string:
    {} places a variable into a string
    0 takes the variable at argument position 0
    : adds formatting options for this variable (otherwise it would represent decimal 6)
    08 formats the number to eight digits zero-padded on the left
    b converts the number to its binary representation
    If you're using a version of Python 3.6 or above, you can also use f-strings: f'{6:08b}'
    """
    print(x)
    x_list = list(x)
    print(x_list)
    last_digit = x_list[len(x_list) - 1]
    print(last_digit)
    if last_digit == 0:
        return True
    else:
        return False


""" 1.3 : Write a short Python function, min_max(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution """


def min_max(data):
    mini = maxi = data[0]

    for item in data:
        if item >= maxi:
            maxi = item
        elif item <= mini:
            mini = item
        else:
            pass

    return mini, maxi


""" 1.4 : Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n """


def sum_square_1():
    input_integer = input('Enter a positive integer: ')
    input_integer = int(input_integer) - 1
    small_ints_list = []
    small_ints_list_squared = []
    total = 0

    while 1 > 0:
        print(input_integer)
        small_ints_list.append(input_integer)
        if input_integer == 0:
            break
        input_integer -= 1

    print(small_ints_list)

    for item in small_ints_list:
        small_ints_list_squared.append(item * item)

    print(small_ints_list_squared)

    for item in small_ints_list_squared:
        total += item

    return total


def sum_square():
    """ Returns sum of square of all positive numbers less than n """
    sqr_sum = 0
    try:
        inp_data = input("Enter a number > ")
        inp_data = int(inp_data)
        if not isinstance(inp_data, int):
            print("input value must be integer")
        elif inp_data <= 2:
            print("Sum of square is 1")
        else:
            for k in range(inp_data):
                sqr_sum += k ** 2
            print("\n\nSum of square of element < %d is %d " % (inp_data, sqr_sum))
    except Exception as ex_cpt:
        print("oh! ", ex_cpt)


""" 1.5 : Give a single command that computes the sum from Exercise R-1.4, relying on Python’s comprehension syntax 
and the built-in sum function. """

# solution 1

# sum(k**2 for k in range(5))

# solution 2 - take user input

# print(sum(k**2 for k in range(int(input('Enter a positive integer: ')))))


""" 1.6 : Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n. """


def odd_sum_squares():
    input_int = input('Enter a positive integer: ')
    try:
        input_int = int(input_int)
    except TypeError as t:
        print('Oh snap!', t)

    num_list = []
    odd_num_list = []
    if input_int <= 2:
        return 'sum of squares is 1'
    else:
        input_int = input_int - 1

        while 1 > 0:
            num_list.append(input_int)
            if input_int is 0:
                break
            input_int -= 1

        for item in num_list:
            if item % 2 != 0:
                odd_num_list.append(item)

        print(odd_num_list)

        print(sum(item ** 2 for item in odd_num_list))


""" 1.7 : Give a single command that computes the sum from Exercise R-1.6, relying on Python’s comprehension syntax 
and the built-in sum function. """


def single_command_odd():
    return sum(k ** 2 for k in range(int(input('Enter a positive integer: '))) if k % 2 != 0)


""" 1.8 : Python allows negative integers to be used as indices into a sequence, such as a string. If string s has 
length n, and expression s[k] is used for index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] 
references the same element? """


def negative_positive():
    s = 'MacBookPro'
    k = -7
    print('s[k] : ', s[k])
    j = len(s) + k
    print('s[j] : ', s[j])


""" 1.9 : What parameters should be sent to the range constructor, to produce a
range with values 50, 60, 70, 80? """


def range_params():
    x = range(50, 90, +10)  # solution
    result = []
    for i in x:
        result.append(i)
    print(result)


""" 1.10 : What parameters should be sent to the range constructor, to produce a
range with values 8, 6, 4, 2, 0, −2, −4, −6, −8? """


def range_params2():
    x = range(8, -10, -2)  # solution
    result = []
    for i in x:
        result.append(i)
    print(result)


""" 1.11 : Demonstrate how to use Python’s list comprehension syntax to produce
the list [1, 2, 4, 8, 16, 32, 64, 128, 256] """


def lis_comp():
    x = [pow(2, k) for k in range(0, 9, +1)]
    print(x)


""" 1.12 : Python’s random module includes a function choice(data) that returns a random element from a non-empty 
sequence. The random module includes a more basic function randrange, with parametrization similar to the built-in 
range function, that return a random choice from the given range. Using only the randrange function, implement your 
own version of the choice function. """


def my_choice(input_data):
    return input_data[random.randrange(0, len(input_data) - 1)]


""" 1.13 : Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function
for doing the same thing. """


# method 1
def reverse_list_1():
    list_in = [1, 3, 4, 9, 5, 7, 6, 10, 8, 2]
    last_index = len(list_in) - 1
    temp_list = []
    while 1 > 0:
        temp_list.append(list_in[last_index])
        if last_index == 0:
            break
        last_index -= 1

    print(temp_list)


# method 2
def reverse_list_2():
    list_in = [1, 3, 4, 9, 5, 7, 6, 10, 8, 2]
    last_index = len(list_in) - 1
    temp_list = []
    for item in range(last_index, -1, -1):
        temp_list.append(list_in[item])

    print(temp_list)


""" 1.14 : Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd. """


def odd_product_ints():
    list_in = [1, 3, 4, 9, 2]
    temp_list = []
    for item in list_in:
        for num in list_in:
            x = item * num
            if x % 2 != 0:
                my_tuple = (item, num)
                temp_list.append(my_tuple)

    print(temp_list)


"""" 1.15 : Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct). """


def check_unique():
    # list_in = [1, 3, 4, 9, 1, 7, 6, 1, 8, 2]
    list_in = [1, 3, 4, 9, 3]
    reverse_list = []
    for item in range(len(list_in) - 1, -1, -1):
        reverse_list.append(item)

    x = list_in & reverse_list
    print(x)


def scale_1(data, factor):
    for j in range(len(data)):
        print(j)
        data[j] *= factor
    print(data)


def scale_2(data, factor):
    for val in data:
        print(val)
        val *= factor
    print(data)


scale_1([1, 2, 3], 5)
scale_2([1, 2, 3], 5)
