# -*- coding: utf-8 -*-
"""
Created on 2025-12-10 02:25:21 UTC+01:00

@author: DiegoCPB
"""

import numpy as np
from scipy import sparse
from scipy.sparse.csgraph import connected_components

def circuits(filepath):
    n = 1000
    C = np.loadtxt(filepath, delimiter=",")
    nC = len(C)
    nD = (nC-1)*nC//2
    D = np.zeros(nD)
    links = np.zeros([nD,2],dtype=int)
    it = 0
    for i in range(nC):
        for j in range(i+1,nC):
            links[it] = [i,j]
            D[it] = np.linalg.norm(C[i]-C[j])
            it += 1
    order = np.argsort(D)
    row,col = links[order][:n].T
    val = np.ones(len(row))
    graph = sparse.csr_array((val,(row,col)),shape=(nC,nC))
    _, labels = connected_components(graph+graph.T, directed=False, return_labels=True)
    _, circuit_lenghts = np.unique(labels,return_counts=True)
    return np.prod(np.sort(circuit_lenghts)[-3:])

if __name__ == "__main__":
    filepath = 'inputs/day8.txt'
    print(circuits(filepath))