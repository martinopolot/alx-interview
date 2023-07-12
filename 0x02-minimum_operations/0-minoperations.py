#!/usr/bin/python3
""" a method that calculates the fewest number of 
operations needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Prototype: def minOperations(n)
    Returns an integer
    All and Paste. Given a number n
    If n is impossible to achieve, return 0
        n: input value
        factor_list: List to save the operations
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)

