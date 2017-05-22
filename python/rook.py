#!/usr/bin/env python
import numpy as np
import sys

def rook(n):
    solutions = []
    if n==1: 
        solutions.append(np.ones((1,1),dtype=int))
    elif n>1:
        solutions.extend(append_rook(rook(n-1)))

    return solutions

def append_rook(sol):
    newsol = []
    for i, s in enumerate(sol):
        n   = s.shape[0]+1
        sn  = np.append(s, np.zeros((n-1,1), dtype=int), axis=1)
        row = np.zeros((1,n), dtype=int)
        row[0,-1] = 1
        for j in range(n):
            newsol.append(np.insert(sn, j, row, axis=0))

    return newsol

def queen(n):
    rk  = rook(n)
    if n<=1: return rk
    sol = []
    for x in rk:
        tr1 = np.array( [np.trace(x, i) for i in range(-n+2, n-1)] )
        tr2 = np.array( [np.trace(x[::-1,:], i) for i in range(-n+2, n-1)] )
        if np.all(tr1<=1) and np.all(tr2<=1): sol.append(x)
    return sol

nsize=int(sys.argv[1])
t=rook(nsize)
for x in t:
    print x
print "found {} rook matrices for size={}".format(len(t), nsize)

t=queen(nsize)
for x in t:
    print x
print "found {} queen matrices for size {}".format(len(t), nsize)
