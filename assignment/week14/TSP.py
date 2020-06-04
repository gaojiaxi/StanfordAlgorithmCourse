# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 16:44:31 2019

@author: gaoji_000
"""

from math import sqrt
from itertools import combinations

class City():
    def __init__(self,city_id,location_x,location_y):
        self.city_id = city_id
        self.location_x = location_x
        self.location_y = location_y
        self.num_cities = 0
    
    def euc_dist(self, city2):
        """Computes the Euclidean distance between 'city1' and 'city2', which are
        2-tuple of coordinates."""

        return sqrt(pow(self.location_x - city2.location_x, 2) + pow(self.location_y - city2.location_y, 2))
    
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
                self.map.append(City(count,float(line.split(' ')[0]),float(line.split(' ')[1])))
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
                

class TSP():
    
    def __init__(self,num_vertex,city_map):
        self.num_vertex = num_vertex
        self.vertex_list = [i for i in range(1,num_vertex+1)]
        self.city_list = city_map
    def comb(self,n,k):
        "For each subset {1..2..n} of size k that contains 1"
        cmb = [(1,) + item for item in combinations(self.vertex_list[1:],k-1)]
        return cmb
    
    def comb_all(self,n):
        cmb_all = []
        for k in range(1,n+1):
            cmb_all.extend(self.comb(n,k))
        return cmb_all
    
    def del_tuple(self,my_tuple,item):
        my_list = list(my_tuple)        
        my_list.remove(item)
        my_tuple = tuple(my_list)
        return my_tuple
        
    def tsp_distance(self,distance_matrix):
        all_subset = self.comb_all(self.num_vertex)
        A = {}
        for subset in all_subset:
            A[subset] = [float('inf') for i in range(self.num_vertex + 1)]
        A[(1,)][1] = 0
        for m in range(2,self.num_vertex + 1):
            for S in self.comb(self.num_vertex,m):
                for j in S[1:]:
                    for k in S:
                        if k != j:
                            A[S][j] = min(A[S][j],A[self.del_tuple(S,j)][k]+distance_matrix[j][k])
        ans = float('inf')
        for j in range(2,self.num_vertex + 1):
            ans = min(ans,A[all_subset[-1]][j] + distance_matrix[1][j])
        return ans

class Solution():
    def run(self,input_file):
        my_map = Map()
        city_map = my_map.read_file(input_file)
        num_vertex = my_map.num_cities
        distance_matrix = my_map.get_pairwise_distance()
        tsp = TSP(num_vertex,city_map)
        res = tsp.tsp_distance(distance_matrix)
        return int(res)

#Final Solution can be obtained using the following three lines of code    
sol = Solution()
res = sol.run('tsp.txt')
print(res)
#Correct answer = [434821, 968, 459, 313, 211]

#In order to test, run the following code in command line
#python tester.py ./assignment/week14/TSP.py ./testCases/course4/assignment2TSP name="run"