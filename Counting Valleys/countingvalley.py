#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    arr=[]
    cont=[]
    count=0
    count2=0
    for i in path:
        arr.append(i)
    for j in arr:
        if j=='U':
            count+=1
        elif j=='D':
            count-=1
        cont.append(count)
    duplct= [i for i, x in enumerate(cont) if x == -1]
    for k in duplct:
        if cont[k+1]==0:
            count2+=1
    # print(cont)
    return(count2)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
