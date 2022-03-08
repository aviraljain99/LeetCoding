"""
Will solve https://leetcode.com/problems/integer-to-roman/
"""

# TODO

def intToRoman(num: int) -> int:
    allRemainder = []

    previousRemainder = 0
    divisor = 10
    remainder = num % divisor

    digit = remainder - previousRemainder
    while remainder != num:
        allRemainder.append(remainder)
