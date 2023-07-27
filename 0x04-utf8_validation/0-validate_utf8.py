#!/usr/bin/python3
"""Write a method that determines if a given data 
set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data will be represented by a list of integers
    Each integer represents 1 byte of data
    Return: True if data is a valid UTF-8 encoding,
    therefore you only need to handle the 8 least significant 
    bits of each integer
    """

    number_of_bytes = 0

    n1 = 1 << 7
    b2 = 1 << 6

    for i in data:
        j = 1 << 7
        if number_of_bytes == 0:
            while j & i:
                number_of_bytes += 1
                j = j >> 1
            if number_of_bytes == 0:
                continue
            if number_of_bytes == 1 or number_of_bytes > 4:
                return False
        else:
            if not (i & n1 and not (i & b2)):
                return False
        number_of_bytes -= 1
    return number_of_bytes == 0
