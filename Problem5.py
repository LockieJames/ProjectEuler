"""
PROBLEM 5

Smallest multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

topNum = 20
num = 1
found = False
smallest = 0

while not found:
    temp = topNum

    b = True

    while temp > 0:
        if num % temp != 0:
            b = False
            break

        temp -= 1

    if b:
        smallest = num
        found = True
    else:
        num += 1

    print(num)

print(smallest)

# The answer is 232792560 (takes forever)

