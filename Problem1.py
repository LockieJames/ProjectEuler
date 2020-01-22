"""
PROBLEM 1

Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def multiples3and5(max):
    sum = 0
    num = 0

    while num < max:
        if num % 3 == 0 or num % 5 == 0:
            sum += num
            num += 1
        else:
            num += 1

    return sum


print(multiples3and5(1000))