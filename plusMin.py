#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive = 0
    negative = 0
    zed = 0
    for i in arr:
        if i > 0:
         positive+=1
        elif i == 0:
            zed+=1
        elif i < 0:
             negative+=1
  
    pDec = positive/len(arr)
    nDec = negative/len(arr)
    zDec = zed/len(arr)
    print(pDec)
    print(nDec)
    print(zDec)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
