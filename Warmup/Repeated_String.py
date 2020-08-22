#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    c=0
    total=0
    for step in s:
        if step=='a':
            c+=1
    ls=len(s)
    total=c*(n//ls)
    rem=n%ls
    for step in s[:rem]:
        if step=='a':
            total+=1
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
