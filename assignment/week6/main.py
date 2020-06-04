# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:13:47 2019

@author: gaoji_000
"""
from heapq import heapify, heappush, heappop
import sys
def make_graph(filename):
    """Make a graph from the data stored inside the text file
    The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200.
    Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge.
    Input: filename - the name of the text file"""

    try: 
        f = open(filename, 'r')
    except IOError:
        sys.exit("No such file!")
    graph={}
    for line in f:
        node=line.split('\t')
        node.remove('\n')
        for i,item in enumerate(node):
            if i==0:
                hash_key=int(item)
                graph[hash_key]=[]
            else:
                graph[hash_key].append((int(item.split(',')[0]),int(item.split(',')[1])))
    f.close()
    return graph

def dijkstra(G, start):
    "Dijkstra algorithm implemeneted using min heap(Also known as priority queue)"
    
    #shortest distances to all nodes.
    D = {}
    #Initialize each node's distance to start to inf.
    for key in G.keys():
        D[key]=float('inf')
    D[start] = 0
    #visited node
    visited = set()
    allnodes=set(G.keys())
    pq= []
    heappush(pq,(0,start))
    
    while visited!=allnodes:
        curr = heappop(pq)[1]
        if curr not in visited:
            visited.add(curr)
        for edge in G[curr]:
            nei = edge[0]
            edgelen = edge[1]
            if nei not in visited:
                curr_dist = D[curr] + edgelen
                if curr_dist < D[nei]:
                    D[nei] = curr_dist
                    heappush(pq,(curr_dist,nei))
    return D
    
    

G = make_graph('dijkstraData.txt')
lst = [7,37,59,82,99,115,133,165,188,197] # a list of all the desired ending vertices
D = dijkstra(G, 1)
for v in lst:
    if v != lst[-1]:
        print(D[v], end=",")
    else:
        print(D[v])
    