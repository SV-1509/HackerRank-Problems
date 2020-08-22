#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr=[0 for i in range(n+1)]
    for q in queries:
        arr[q[0]-1]+=q[2]
        arr[q[1]]-=q[2]
    max_val=arr[0]
    val=0
    for i in arr:
        val+=i
        if val>max_val:
            max_val=val
    return max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
