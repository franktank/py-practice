"""
The fuel control mechanisms have three operations:

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called answer(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
answer(4) returns 2: 4 -> 2 -> 1
answer(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1


Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) n = "4"
Output:
    (int) 2

Inputs:
    (string) n = "15"
Output:
    (int) 5
"""
def answer(n):
    return helper(int(n))

def answer(n):
    if n < 0:
        return -1
    return helper(int(n))

def helper(n):
    counter = 0
    while n != 1:
        if n & 1 == 0:
            n = n >> 1
        elif n < 4 or  n % 4 == 1:
            n -= 1
        else:
            n += 1
        counter += 1
    return counter

def helper(n):
    if n == 1:
        return 0
    if n%2 == 0:
        return 1 + helper(n/2)
    elif n%4 == 1:
        return 1 + helper(n-1)
    else:
        return 1 + helper(n+1)
