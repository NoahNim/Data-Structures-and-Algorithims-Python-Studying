#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pol_notation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY tokens as parameter.
#

from collections import deque


def pol_notation(tokens):
    # Write your code here
    # create a stack
    # loop through tokens check if token is not an operator, if it is not then append to stack
    # else if it is an operator, make a right and left variable from stack.pop() then check what kinda operation the token is
    # then append the result of left and right of that operation
    # return the number
    stack = deque([])
    for token in tokens:
        if token not in '/*+-':
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            elif token == '-':
                stack.append(left - right)
            elif token == '*':
                stack.append(left * right)
            elif token == '/':
                stack.append(int(left / right))
    return stack.pop()