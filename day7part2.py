# -*- coding: utf-8 -*-
"""
Created on 2025-12-07 12:23:17 UTC+01:00

@author: DiegoCPB
"""

def beam_splits(filepath):
    with open(filepath) as file:
        table = []
        for line in file:
            table_i = []
            for char in list(line.strip('\n')):
                if char=='^': table_i.append(-1)
                elif char=='.': table_i.append(0)
                else: table_i.append(1)
            table.append(table_i)
    counter = 0
    for i in range(1,len(table)):
        for j in range(len(table[0])):
            if table[i][j] >= 0:
                table[i][j] += table[i-1][j]
            elif table[i][j] == -1:
                table[i][j] = 0
                table[i][j-1] += table[i-1][j]
                table[i][j+1] += table[i-1][j]
    return sum(table[-1])

if __name__ == "__main__":
    filepath = 'tests/day7.txt'
    print(beam_splits(filepath))