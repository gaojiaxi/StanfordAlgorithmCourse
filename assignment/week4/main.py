# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:02:33 2019

@author: gaojiaxi
"""
import random
import copy

class Solution():
    
    def run(self,input_file):
        graph = {}
        for line in open(input_file):
            line = line.strip()
            node=line.split(' ')
            node = [int(item) for item in node]
            graph[node[0]]=node[1:]
        mc = MinCut()
        res = mc.run_multiple(graph,10000)
        return res
    
class MinCut():
    def __init__(self):
        self.min_cut = float('inf')
    
    def test(self,input_file):
        graph = {}
        for line in open(input_file):
            line = line.strip()
            node=line.split('\t')
            node = [int(item) for item in node]
            graph[node[0]]=node[1:]
        self.run_multiple(graph,10000)
        return self.min_cut
    
    def run_multiple(self,graph,num_exp):
        for i in range(num_exp):
            graph_cp = copy.deepcopy(graph)
            cur_cut=self.contraction(graph_cp)
            self.min_cut = min(self.min_cut,cur_cut)
        return self.min_cut
        
        
        
        
    def contraction(self,graph):
        while(len(graph.keys())>2):
            key1=random.sample(graph.keys(),1)[0]
            key2=random.sample(graph[key1],1)[0]
            if key2 in graph[key1]:
                graph[key1].remove(key2)
            if key1 in graph[key2]:
                graph[key2].remove(key1)
            graph[key1].extend(graph[key2])
            graph.pop(key2, None)
            for key in graph.keys():
                new_connection = graph[key]
                while key2 in new_connection:
                    new_connection.remove(key2)
                    new_connection.append(key1)
                
                while key in new_connection:
                    new_connection.remove(key)
                
                graph[key]=new_connection
                
                        
        return len(graph[list(graph.keys())[0]])
#In order to test, run the following code in command line
#python tester.py ./assignment/week4/main.py ./testCases/course1/week4MinCut name="run"

#Final Solution can be obtained using the following two lines of code
#sol = Solution()
#min_cut=sol.test('kargerMinCut.txt')
#Correct answer = 17
