# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 12:32:10 2019

@author: gaoji_000
"""

from operator import attrgetter
import sys 
sys.path.append("C:\\Users\\gaoji_000\\Desktop\\assigment_coursera_algorithm") 
from util.datastructure.union_find import UnionFind


class ClusterFinder(object):

    def __init__(self, input_file):
        with open(input_file, 'r') as file:
            self._num_vertices = int(file.readline())
            self._edges = []
            for line in file:
                edge_from, edge_to, cost = line.split()
                self._edges.append(Edge(int(edge_from), int(edge_to), int(cost)))

    def find_clusters(self, count):
        sorted_edges = sorted(self._edges, key=attrgetter("cost"))
        uf = UnionFind(self._num_vertices)
        for index, edge in enumerate(sorted_edges):
            if count != uf.count and not uf.connected(edge.from_vertex, edge.to_vertex):
                uf.union(edge.from_vertex, edge.to_vertex)
            if uf.count == count and not uf.connected(edge.from_vertex, edge.to_vertex):
                return edge.cost,uf._uf


class Edge:
    def __init__(self, edge_from, edge_to, cost):
        self.from_vertex = edge_from
        self.to_vertex = edge_to
        self.cost = cost


if __name__ == "__main__": 
    cluster_finder = ClusterFinder("clustering1.txt")
    distance,uf=cluster_finder.find_clusters(4)
    