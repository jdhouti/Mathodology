# Julien Dhouti
# Started: October 30, 2016
# This script is a class of math functions re-written my way.

import math
import time
import ListFunctions as lf

def factorial(number):
    """Finds the factorial of a given number."""
    if number == 0:
        return 1

    else:
        return number * (factorial(number - 1))

def factorialv2(x):
    """A factorial function written a different way."""
    u = x - 1

    while u != 0:
        x = x * u
        u -= 1
    return x

def power(number, exponent):
    """Returns the power of a number given its power n."""
    if exponent == 0:
        return 1

    else:
        return number * (power(number, exponent - 1))

def sum(n1, n2):
    """Returns the sum of two given numbers."""

    return n1 + n2

def sum_up_to(n):
    """This is like factorial but for addition instead of multiplication"""
    if n == 0:
        return 0

    else:
        return n + sum_up_to(n)

def absv(n):
    """Returns the absolute value of a given number."""
    if n < 0:
        return -(n)

    else:
        return n

def distance(n1, n2):
    """Returns the distance between two given numbers."""

    return absv(n2 - n1)

def sub(n1, n2):
    """Returns the difference between two given numbers (n2 - n1)."""

    return n2 - n1

def quadratic(a, b, c):
    """Returns the two answers to a quadratic equation given the a, b and, c of the equation."""
    numeratorP = -b + math.sqrt(power(b, 2) - (4 * a * c))
    numeratorN = -b - math.sqrt(power(b, 2) - (4 * a * c))
    denominator = 2 * a

    a1 = numeratorP / denominator
    a2 = numeratorN / denominator

    # !Returns two values!
    return a1, a2

def circle_area(radius):
    """Returns the area of a circle given it's radius."""
    return round(power(radius, 2) * PI, 2)

def cylinder_volume(r, h):
    """Returns the volume of a cylinder given its radius (r) and height (h)."""
    return PI * (r * r) * h

def is_even(n):
    """Returns True if a given integer is even, returns False otherwise."""
    if n % 2 == 0:
        return True

    else:
        return False

def sum_natural(n):
    """Returns the sum of all of the natural numbers below and included to a given natural number."""
    total, k = 0, 1

    while k <= n:
        total = k + total
        k += 1

    return total

def sum_cubes(n):
    total, k = 0, 1

    while k <= n:
        total = (k * k * k) + total
        k += 1

    return total

def is_dec(n):
    """Checks if a given number is a decimal or not."""
    if n % 1 == 0:
        return False

    else:
        return True

# Not accurate + not stable
def my_sqrt(x):
    """This function will find the sqrt of a number."""
    return pow(x, 0.5)

def sqrt_proof(x):
    """This function proves the exponential nature of the sqrt function.
    It shows that no matter how big x is, the result will always be around 60."""
    counter = 0

    while x != 1:
        x = math.sqrt(x)
        counter += 1
        print(x)

    return counter

def round_5(x):
    return round(x, 5)

# CONSTANTS
PI = 3.14159265358979323846264338327950288419716939937510582097494459230781640
