# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 10:38:45 2019

@author: gaoji_000
"""

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = []

def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)