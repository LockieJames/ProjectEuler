"""
PROBLEM 6

Sum square difference

The sum of the squares of the first ten natural numbers is,
1^2+2^2+...+10^2=385

The square of the sum of the first ten natural numbers is,
(1+2+...+10)^2=552=3025

Hence the difference between the sum of the squares of the first ten natural number
and the square of the sum is 3025−385=2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

num = 100
sumOfSquares = 0
squareOfSum = 0
answer = 0

for i in range(1, num + 1):
    sumOfSquares = i**2 + sumOfSquares
    squareOfSum += i

answer = squareOfSum**2 - sumOfSquares

print(answer)


# Answer is 25164150


