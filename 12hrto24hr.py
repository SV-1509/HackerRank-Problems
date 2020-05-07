#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):

    if s[-2:]=="PM" and s[:2]!="12":
        a=int(s[:2])
        a=str(a+12)
        s.replace('PM','')
        s=a+s[2:]
    if s[-2:]=="AM" and s[:2]=="12": 
        d="00"
        s.replace('AM','')
        s=d+s[2:]   
        

    return s[:-2]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
