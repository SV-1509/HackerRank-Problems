#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    bribe=0
    c=0
    tes=[i for i in range(1,len(q)+1)]
    while tes!=[]:
        if q[0]==tes[0]:
            tes.pop(0)
            q.pop(0)
        elif q[0]==tes[1]:
            bribe+=1
            tes.pop(1)
            q.pop(0)
        elif q[0]==tes[2]:
            bribe+=2
            tes.pop(2)
            q.pop(0)
        else:
            c=1
            break
    if c==0:        
        print(bribe)
    elif c==1:
        print('Too chaotic')



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
