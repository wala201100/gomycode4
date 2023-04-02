#Question 1
def find_max(a, b, c):
    """Returns the largest of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    # Question 2
    def calculation(a, b):
        """Returns the addition and subtraction of two variables."""
        add = a + b
        sub = a - b
        return add, sub
# Question 3
def sum_list(lst):
    """Sums the elements of a list of integers."""
    return sum(lst)

def multiply_list(lst):
    """Multiplies the elements of an integer list."""
    product = 1
    for num in lst:
        product *= num
    return product
def sum_even_multiply_odd(lst):
    """Sums the even-indexed elements and multiplies the odd-indexed elements of a list."""
    even_list = lst[::2]  # get every even-indexed element
    odd_list = lst[1::2]  # get every odd-indexed element
    even_sum = sum_list(even_list)  # sum the even-indexed elements
    odd_product = multiply_list(odd_list)  # multiply the odd-indexed elements
    return even_sum, odd_product
#   example
    lst = [2, 3, 5, 7, 11, 13, 17, 19]
    sum_even_multiply_odd(lst)
(30, 19210725)
# Question 4
def capitalize_first_letter_values(dct):
    """Displays the first letter of each dictionary value in upper case."""
    result = {}
    for key, value in dct.items():
        result[key] = value.capitalize()[0]
    return result
    #   example
    dct = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red'}
    capitalize_first_letter_values(dct)
{'apple': 'R', 'banana': 'Y', 'cherry': 'R'}

# Question 5
def largest_word(dct):
    """Returns the largest word in a dictionary."""
    largest = ""
    for key in dct.keys():
        if len(key) > len(largest):
            largest = key
    return largest
    #   example
    dct = {'apple': 'red', 'banana': 'yellow', 'cherry': 'red', 'strawberry': 'red'}
    largest_word(dct)
'strawberry'
# Question 6
seq = input("Enter a hyphen-separated sequence of words: ")

words = seq.split("-")  # split the input string into a list of words
words.sort()  # sort the list of words alphabetically

result = "-".join(words)  # join the sorted list of words back into a hyphen-separated string

print(result)
# Question 7
import math

def calculate_Q(D_values):
    C = 50
    H = 30
    D_list = D_values.split(",")
    Q_list = []
    for D in D_list:
        Q = round(math.sqrt((2*C*int(D))/H))
        Q_list.append(Q)
    return ",".join(str(Q) for Q in Q_list)
print(calculate_Q("100,150,180"))











