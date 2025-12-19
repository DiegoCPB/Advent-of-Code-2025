# -*- coding: utf-8 -*-
"""
Created on 2025-12-12 20:58:02 UTC+01:00

@author: DiegoCPB
"""

from collections import defaultdict

def count_paths_topo(graph, start, end):
    indegree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    q = [u for u in graph if indegree[u] == 0]
    topo = []
    while q:
        u = q.pop(0)
        topo.append(u)
        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)
    dp = defaultdict(int)
    dp[start] = 1
    for u in topo:
        for v in graph.get(u, []):
            dp[v] += dp[u]
    return dp[end]

def svr2out(filepath):
    links = {}
    res = 1
    with open(filepath) as file:
        for line in file:
            if line.rstrip():
                words = line.split()
                links[words[0][:-1]] = words[1:]
    res *= count_paths_topo(links,'svr','fft')
    res *= count_paths_topo(links,'fft','dac')
    res *= count_paths_topo(links,'dac','out')
    return res

if __name__ == "__main__":
    filepath = 'inputs/day11.txt'
    print(svr2out(filepath))