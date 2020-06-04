# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:36:19 2020

@author: gaojiaxi
"""

from math import sqrt
from heapq import heapify, heappush, heappop

class City():
    def __init__(self,city_id,location_x,location_y):
        self.city_id = city_id
        self.location_x = location_x
        self.location_y = location_y
        self.num_cities = 0
    
    def euc_dist(self, other):
        """Computes the Euclidean distance between 'city1' and 'city2', which are
        2-tuple of coordinates."""

        return sqrt(pow(self.location_x - other.location_x, 2) + pow(self.location_y - other.location_y, 2))
    
class Map():
    def __init__(self):
        self.map = []
        self.num_cities = 0
    def read_file(self,input_file):
        self.map = [City(0,0,0)]
        for line in open(input_file):
            if len(line.split(' '))==1:
                self.num_cities = int(line)
                count = 1
            else:
                self.map.append(City(count,float(line.split(' ')[1]),float(line.split(' ')[2])))
                count += 1
        return self.map
    def get_pairwise_distance(self):
        if not self.map:
            print("map is empty!")
            return None
        distance_matrix = [[0 for i in range(self.num_cities+1)] for j in range(self.num_cities+1)]
        for i in range(1,self.num_cities+1):
            for j in range(1,self.num_cities+1):
                distance_matrix[i][j] = self.map[i].euc_dist(self.map[j])
        return distance_matrix

class Edge():
    def __init__(self,length,start,end):
        self.length = length
        self.start = start
        self.end = end
    def __lt__(self, other):
        if self.length < other.length:
            return True
        elif self.length == other.length:
            if self.end < other.end:
                return True
        return False
    
class TSP():
    def __init__(self,num_city,city_list):
        self.num_city = num_city
        self.city_list = city_list
        
    def greedy(self,start):
        "greedy algorithm implemeneted using min heap(Also known as priority queue)"
        
        #visited node
        visited = set()
        allnodes=set([i for i in range(1,self.num_city+1)])
        
        pq = [Edge(self.city_list[start].euc_dist(self.city_list[j]),start,j) for j in range(1,1+self.num_city) if j!= start]
        heapify(pq)
        visited.add(start)
        tsp_dist = 0
        while visited!=allnodes:
            curr_edge = heappop(pq)
            visited.add(curr_edge.end)
#            if len(visited) % 1000 ==0:
#                print("finished:%s nodes"%(len(visited)))
            tsp_dist += curr_edge.length
            pq = [Edge(self.city_list[curr_edge.end].euc_dist(self.city_list[j]),curr_edge.end,j) for j in range(1,self.num_city+1) if j!= curr_edge.end and j not in visited]
            heapify(pq)
        tsp_dist += self.city_list[curr_edge.end].euc_dist(self.city_list[1])
        return tsp_dist

class Solution():
    def run(self,input_file):
        my_map = Map()
        city_list= my_map.read_file(input_file)
        num_vertex = my_map.num_cities
        tsp = TSP(num_vertex,city_list)
        res = tsp.greedy(1)
        return int(res)

#Final Solution can be obtained using the following two lines of code
#sol = Solution()
res = sol.run('nn.txt')
print("correct answer is" + str(res))
#Correct answer = 1203406

#In order to test, run the following code in command line
#python tester.py ./assignment/week15/main.py ./testCases/course4/assignment3TSPHeuristic name="run"