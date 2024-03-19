#!/usr/bin/python3
"""In a txt file, there is a single char H.
 Your text editor can execute only two operations
 in this file: Copy All and Paste. Given a num
n, write a method that calculates the fewest nums
of operations needed to result in exactly n H
chars in the file."""


def minOperations(n: int) -> int:
    """calculates the fewest number of operations
    needed to result in exactly n H chars
    in the file"""
    process = 2
    op = 0
    while n > 1:
        while n % process == 0:
            op += process
            n /= process
        process += 1
    return op
