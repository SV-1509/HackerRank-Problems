#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count=0
    i=0
    while i<len(c):
        if i==len(c)-1:
            return count
        elif i==len(c)-2:
            return count+1
        elif c[i+2]==1:
            count+=1
            i+=1
        elif c[i+2]==0:
            count+=1
            i+=2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
