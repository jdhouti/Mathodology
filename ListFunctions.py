# Julien Dhouti
# Started: October 30, 2016
# This script is a class of math functions applied to lists.
import BoolFunctions

# Will return the median in a function.
import NumMath

def list_median(li):
    """Returns the median of a given numerical list."""
    li.sort()

    if len(li) % 2 == 0:                # If the length of the list is even,
        fHalf = li[:len(li) / 2]        # Obtain the first half
        sHalf = li[len(li) / 2:]        # and then the second half
        return (fHalf[-1] + sHalf[0]) / 2.0
    else:
        answer = li[:(len(li) / 2) + 1]
        return answer[-1]

def list_sum(li):
    """Return the sum of all elements in a given numerical list."""
    total = 0
    for ele in li:
        total += ele
    return total

def list_mean(li):
    """Returns the mean of all of the elements in a given numerical list."""
    return list_sum(li) / float(len(li))

def list_range(li):
    """Returns the range of a given numerical list."""
    li.sort()
    return abs(li[-1] - li[0])

def list_prod(li):
    """Returns the total product of every element in a given numerical list."""
    total = 0
    for ele in li:
        total *= ele
    return total

def list_sum_square(li):
    """Returns the sum of all of the values in a given numerical list, squared."""
    newList = []
    for i in li:
        newList.append(i**2)
    return list_sum(newList)

def list_square(li):
    """Returns a list of all of the values from a given numerical list, squared."""
    newList = []
    for i in li:
        newList.append(i**2)
    return newList

def list_filter_even(li):
    """Returns only the even integers of a given numerical list."""
    newList = []
    for i in li:
        if i % 2 == 0:
            newList.append(li[i])
    return newList

def list_filter_True(bool_list):
    """Returns only the true booleans in a given boolean list."""
    newList = []
    for boolean in bool_list:
        if boolean:
            newList.append(boolean)
    return newList

# This is a higher order function
# This will combine two different lists given a basic numerical function
def list_combination(func, l1, l2):
    newList = []
    for i, j in l1, l2:
        newList.append(func(i, j))
    return newList

# This function uses a higher order function
def list_mult_index(l1, l2):
    """Returns the product of each given index in two given numerical list, in one list."""
    return list_combination(NumMath.prod, l1, l2)

# This function uses a higher order function
def list_sum_index(l1, l2):
    """Returns the sum of each given index in two given numerical list, in one list."""
    return list_combination(NumMath.sum, l1, l2)

# This function uses a higher order function
def list_distance_index(l1, l2):
    """Returns the distance between each given index in two given numerical list, in one list."""
    return list_combination(NumMath.distance, l1, l2)

# This is a higher order function!
# It will apply the given "func" to every element in "l"!
def list_func(func, li):
    """This will apply a function to every element in a list."""
    newList = []
    for i in li:
        newList.append(func(i))
    return newList

# # Mutator method!
# def list_inc(l, n):
#     """Increments every element in a list by a given number."""
#     return list_one_by_one(n.sum, l, n)
#
# # Mutator method!
# def list_mult(l, n):
#     """Multiplies every element in a given numerical list by a given number."""
#     return list_one_by_one(n.prod, l, n)
#
# # Mutator method!
# def list_dec(l, n):
#     """Deducts a given amount from every element in a list."""
#     return list_one_by_one(n.sub, l, n)

def check_sorted(l):
    """Checks if a given list l is sorted."""
    for i in range(0, len(l) - 1):
        if l[i] > l[i+1]:
            return False
    return True

def list_eq(l1, l2):
    """Returns True if both given numerical lists are identical. False otherwise."""
    ## Version 2.0
    if len(l1) != len(l2):
        return False

    for i in range(0, len(l1)):
        if l1[i] == l2[i]:
            pass
        else:
            return False
    return True

def list_reverse(l):
    """This function returns the reverse of any given lists."""
    ## Version 2.0
    newList = []

    for i in range(1, len(l) + 1):
        newList.append(l[-i])
    return newList

def list_range_by_to(start, dec, end):
    """Returns a list of all items between end and start in intervals of dec. Decreasing order."""
    newList, c = [], start

    while c >= end:
        newList.append(c)
        c -= dec
    return newList

def some_even(l):
    """Checks if a numerical list contains any even numbers. Returns True if it does."""
    ## Version 2.0
    for i in range(0, len(l)):
        if l[i] % 2 == 0:
            return True
        else:
            pass
    return False

def all_even(l):
    """Checks if a numerical lists ONLY contains even numbers. Returns True if it does."""
    ## Version 2.0
    for i in range(0, len(l)):
        if l[i] % 2 == 0:
            pass
        else:
            return False
    return True

# def list_is_palindrome(l):
#     """Function that tests whether a given string or list (of any type) is a palindrome."""
#     if isinstance(l, basestring):       # simply converts a string into a list
#         l = list(l)
#
#     for i in range(0, ((len(l) - 1) / 2) + 1):
#         if l[i] != l[-(i + 1)]:
#             return False
#     return True

# this is higher order function
def list_convert(l1, func):
    """Applies a function to every element in a given numerical list."""
    ## Version 2.0
    newList = []

    for i in range(0, len(l1)):
        newList.append(func(l1[i]))
    return newList

def append_lists(l1, l2):
    """Appends a given numerical list to another numerical list."""
    """This function will not return a list within a list."""
    ## Version 2.0
    for i in range(0, len(l2)):
        l1.append(l2[i])

    l1.sort()
    return l1

def find_largest_element(l):
    """Finds the largest element in a given numerical list."""
    smallest = l[0]

    for i in range(1, len(l)):
        if l[i] > largest:
            largest = l[i]
    return largest

def list_len(l):
    """Counts the length of a given list."""
    length = 0

    for i in l:
        length += 1
    return length

def list_element_count(l, a):
    """Counts the amount of times a appears in a list."""
    count = 0

    for i in range(0, len(l)):
        if l[i] == a:
            count += 1
    return count


myList_test = [1, 2, 3, 4, 5, 6, 6, 4]

print(list_square(myList_test))
