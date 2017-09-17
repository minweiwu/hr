#!/usr/bin/env python
import sys
import numpy as np
def board(m,n):
    return np.zeros([m,n]).astype(bool)

def flip(board,i,j):
    board[i][j]=not board[i][j]
    return board

def test(board,i=0,j=0):
    m,n = board.shape
    flip(board, i,j)
    if i==m-1 and j==n-1:
        return 1
    else:
        ret = 0
        for i1,j1 in [(-1,0),(1,0),(0,-1),(0,1)]:
            if i+i1<0 or i+i1>=m or j+j1<0 or j+j1>=n: continue
            if board[i+i1][j+j1]: continue
            ret += test(np.array(board), i+i1, j+j1)
        return ret


if __name__=='__main__':
    if len(sys.argv)==2:
        m = n = int(sys.argv[1])
    else:
        m, n = map(int, sys.argv[1:3])
    b = board(m,n)
    print m, n, test(b)
