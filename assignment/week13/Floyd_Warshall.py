# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:15:44 2019

@author: gaoji_000
"""



import numpy as np

class Edge():
    def __init__(self,tail,head,weight):
        self.tail = tail
        self.head = head
        self.weight = weight

class Solution():
    def read_file(self,input_file):
    
        G={}
    
        for line in open(input_file):
            if line != '\n' and len(line.split(' '))==2:
                num_nodes=int(line.split(' ')[0])
                num_edges=int(line.split(' ')[1])
            elif line != '\n':
                edge = Edge(int(line.split(' ')[0]),int(line.split(' ')[1]),int(line.split(' ')[2]))
                if (edge.tail,edge.head) not in G:
                    G[(edge.tail,edge.head)] = edge.weight
                else:
                    if G[(edge.tail,edge.head)] > edge.weight:
                        G[(edge.tail,edge.head)] = edge.weight
        return G,num_nodes
    
    def Floyd_Warshall(self,input_file):
        G,num_nodes = self.read_file(input_file)
        
        A=np.zeros((num_nodes+1,num_nodes+1,num_nodes+1))
        global_min = float('inf')

        for i in range(1,num_nodes+1):
            for j in range(1,num_nodes+1):
                    if i==j:
                        A[i,j,0]=0
                    elif (i,j) in G.keys():
                        A[i,j,0]=G[(i,j)]
                    else:
                        A[i,j,0]=float('inf')
        
        for k in range(1,num_nodes+1):
            for i in range(1,num_nodes+1):
                for j in range(1,num_nodes+1):
                    A[i,j,k]=min(A[i,j,k-1],A[i,k,k-1]+A[k,j,k-1])
                    global_min = min(global_min,A[i,j,k])
        
        global_min = int(global_min)
        
        for i in range(1,num_nodes+1):
            if A[i,i,num_nodes]<0:
                print('there is a negative cycle for the input graph!')
                global_min = 'NULL'
                break
        
        return global_min
    def run(self,input_file):
        global_min = self.Floyd_Warshall(input_file)
        return global_min
    
#sol = Solution()
#G = sol.run('g3.txt')
#import pandas as pd
#import numpy as np
#
#graph_df={}
#
#for line in open('g1.txt'):
#    if line != '\n' and len(line.split(' '))==2:
#        num_node=int(line.split(' ')[0])
#        num_edge=int(line.split(' ')[1])
#    elif line != '\n':
#        graph_df[(int(line.split(' ')[0]),int(line.split(' ')[1]))] = int(line.split(' ')[2])
#        
#        
#A=np.zeros((num_node+1,num_node+1,num_node+1))
#
#
#for i in range(1,num_node+1):
#    for j in range(1,num_node+1):
#            if i==j:
#                A[i,j,0]=0
#            elif (i,j) in graph_df.keys():
#                A[i,j,0]=graph_df[(i,j)]
#            else:
#                A[i,j,0]=float('inf')
#
#for k in range(1,num_node+1):
#    for i in range(1,num_node+1):
#        for j in range(1,num_node+1):
#            A[i,j,k]=min(A[i,j,k-1],A[i,k,k-1]+A[k,j,k-1])
#
#
#for i in range(1,num_node+1):
#    if A[i,i,num_node]<0:
#        print('there is a negative cycle for the input graph!')
#        break
#print(A[1:,1:,num_node])

#there is a negative cycle for the g1!
#there is a negative cycle for the g2!