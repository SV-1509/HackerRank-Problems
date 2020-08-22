#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar.sort()
    count=0
    while ar!=[]:
        if len(ar)==1:
            return count
        if ar[0]==ar[1]:
            count+=1
            ar.pop(0)
            ar.pop(0)
        else:
            ar.pop(0)
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
