# -*- coding: utf-8 -*-
"""
Created on 2025-12-10 18:26:26 UTC+01:00

@author: DiegoCPB
"""

import numpy as np

def rectangles(filepath):
    C = np.loadtxt(filepath, delimiter=",",dtype=int)
    nC = len(C)
    maxA = 0
    for i in range(nC):
        for j in range(i+1,nC):
            d  = np.abs(C[i]-C[j])
            itA = (d[0]+1)*(d[1]+1)
            maxA = np.max([itA,maxA])
    return maxA

if __name__ == "__main__":
    filepath = 'inputs/day9.txt'
    print(rectangles(filepath))