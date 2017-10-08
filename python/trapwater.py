#!/usr/bin/env python
import sys
import numpy as np
"""
http://www.geeksforgeeks.org/trapping-rain-water/
"""

def trap(arr):
    ret  = 0
    rmax = 0
    sidx = 0
    for i,x in enumerate(arr):
        if x>=rmax: #water block should end here
            if i>sidx+1: ret += (i-sidx-1)*rmax-sum(arr[sidx+1:i])
            rmax = x
            sidx = i
        else:
            continue
    if i>sidx+1: ret+=trap(arr[i:sidx-1:-1])
    return ret

if __name__=='__main__':
    arr = map(int, sys.argv[1:])
    print arr
    print trap(arr)
