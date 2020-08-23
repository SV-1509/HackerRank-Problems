#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    ar = sorted(arr)
    index = {a: i for i,a in enumerate(arr)}
    moves = 0
    
    for i,a in enumerate(arr):
        correct_value = ar[i]
        if a!= correct_value:
            to_swap_ix = index[correct_value]
            arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
            index[a] = to_swap_ix
            index[correct_value] = i
            moves += 1
            
    return moves

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
