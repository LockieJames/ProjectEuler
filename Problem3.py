"""
PROBLEM 3

Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

i = 0
num = 600851475143
largest = 0

while i < num:
    i += 1

    if (num/i).is_integer():
        if i > largest:
            largest = i

        num = num/i


print(largest)

# The answer is 6857

