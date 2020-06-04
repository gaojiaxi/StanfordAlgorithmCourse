# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 14:59:39 2019

@author: gaoji_000
"""

graph={}
V=[]

for line in open('edges.txt'):
    if len(line.split(' '))==2:
        nums_node=int(line.split(' ')[0])
        nums_edge=int(line.split(' ')[1])
    else:
        graph[(int(line.split(' ')[0]),int(line.split(' ')[1]))]=int(line.split(' ')[2])
        graph[(int(line.split(' ')[1]),int(line.split(' ')[0]))]=int(line.split(' ')[2])
        if int(line.split(' ')[0]) not in V:
            V.append(int(line.split(' ')[0]))
        if int(line.split(' ')[1]) not in V:
            V.append(int(line.split(' ')[1]))
#initialize X (contains an arbitary node in set X)
X=[1]
V.remove(1)
total_cost=0
while V:
    cur_min=1000000000000
    cur_head=None
    for tail in X:
        for head in V:
            if (tail,head) in graph.keys() and graph[(tail,head)]<cur_min:
                cur_min=graph[(tail,head)]
                cur_head=head
#            if (head,tail) in graph.keys() and graph[(head,tail)]<cur_min:
#                cur_min=graph[(head,tail)]
#                cur_head=tail
    total_cost+=cur_min
    X.append(cur_head)
    V.remove(cur_head)


        