# Julien Dhouti
# Started: October 30, 2016
# This script is a class of math functions re-written my way.

import math
import time

# not really a math function.
def whichIsFaster(func1, func2):
    z = 0
    f1, f2 = 0, 0

    while z < 101:
        x, y = 0, 0
        firstFuncT, secondFuncT = 0, 0

        # calculate speed for first function
        while x < 101:
            start = time.time()
            func1
            end = time.time()

            x += 1
            firstFuncT += (end - start)

        firstFuncT = firstFuncT / 100.0

        #calculate the speed for the second function
        while y < 101:
            start = time.time()
            func2
            end = time.time()

            y += 1
            secondFuncT += (end - start)

        secondFuncT = secondFuncT / 100.0

        if firstFuncT < secondFuncT:
            f1 += 1

        elif secondFuncT < firstFuncT:
            f2 += 1

        else:
            pass

        z += 1

    # determine which was faster
    if distance(f1, f2) <= 15:
        return "Both functions were equally fast.", "Speed >> " + str(firstFuncT)

    elif f1 > f2:
        return "First function was faster.", "Speed >> " + str(firstFuncT)

    else:
        return "Second function was faster.", "Speed >> " + str(secondFuncT)

def factorial(number):
    """Finds the factorial of a given number."""
    if number == 0:
        return 1

    else:
        return number * (factorial(number - 1))

def factorialTwo(x):
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
    if n == 0:
        return 0

    else:
        return n + sum_up_to(n)

def prod(n1, n2):
    """Returns the product of two given numbers."""

    return n1 * n2

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

    return PI * (radius * radius) * h

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

PI = 3.14159265358979323846264338327950288419716939937510582097494459230781640
