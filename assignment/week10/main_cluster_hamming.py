# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 15:16:59 2019

@author: gaoji_000
"""

import pandas as pd
import numpy as np
import copy
from itertools import combinations

def flip_bit(bit):
    if bit == 1:
        return 0
    if bit == 0:
        return 1


def hamming_possibilities(node, distance):
    """Calculate all possible nodes within a hamming distance of node"""
    idxs = combinations(range(len(node)), distance)
    nodes = list()
    for shift in idxs:
        new = copy.copy(node)
        for pos in shift:
            new[pos] = flip_bit(node[pos])
        nodes.append(new)
    return nodes


node=[0 for i in range(24)]
nodes=hamming_possibilities(node, distance=1)
nodes_2=hamming_possibilities(node, distance=2)
nodes.extend(nodes_2)

added_value=[]
for node in nodes:
    res = int("".join(str(x) for x in node), 2) 
    added_value.append(res)


node_dict={}    
node_id=1    
for line in open('clustering_big.txt'):
    if line != '\n' and len(line.split(' '))==2:
        num_node,num_bits=int(line.split(' ')[0]),int(line.split(' ')[1])
    elif line != '\n':
        node=[int(item) for item in line.split(' ')[:-1]]
        node_val= int("".join(str(x) for x in node), 2)
        if node_val not in node_dict.keys():
            node_dict[node_val]=[node_id]
        else:
            node_dict[node_val].append(node_id)
        node_id+=1

columns = ['Node','Leader', 'LeaderSize']
Union_find_df=pd.DataFrame(columns=columns)
for i in range(1,num_node+1):
    Union_find_df = Union_find_df.append(pd.Series([i,i,1], index=Union_find_df.columns), ignore_index=True)
Union_find_df.set_index(keys='Node',inplace=True)

for key in node_dict.keys():
    for add_val in added_value:
        if key+add_val in node_dict.keys() and Union_find_df.loc[node_dict[key][0]]['Leader'] != Union_find_df.loc[node_dict[key+add_val][0]]['Leader']:
            
            


        