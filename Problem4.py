"""
PROBLEM 4

Largest palindrome product

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

num1 = 1
num2 = 1
numOfDigits = 4
largest = 0

while len(str(num1)) < numOfDigits + 1:
    while len(str(num2)) < numOfDigits + 1:
        product = num1 * num2
        productStr = str(product)
        productSize = len(productStr)

        start = 0
        end = productSize - 1

        same = True

        while start < productSize:
            if productStr[start] != productStr[end]:
                same = False

            start += 1
            end -= 1

        if same and product > largest:
            largest = product

        num2 += 1

    num1 += 1
    num2 = 0

print(largest)

# The answer is 906609

