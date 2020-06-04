# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 15:49:53 2019

@author: gaoji_000
"""
import sys,collections
import resource
sys.setrecursionlimit(10000000)

resource.setrlimit(resource.RLIMIT_STACK, (2**26, 2**27))

class Graph():

    
    def __init__(self):
        self.adjListMap = {}
        self.num_nodes = 0
        self.nodes = set()

    
    def add_edge(self,tail,head):
        if tail not in self.adjListMap:
            self.adjListMap[tail] = [head]
        else:
            self.adjListMap[tail].append(head)
        
        self.add_node(tail)
        self.add_node(head)
    
    
    def add_node(self,node):
        if node not in self.nodes:
            self.nodes.add(node)
        self.num_nodes = len(self.nodes)
    
    
    def add_isolated_nodes(self):
        max_node_index = max(self.nodes)
        if max_node_index > len(self.nodes):
            isolate_nodes = set([i for i in range(1,max_node_index + 1)])-self.nodes
            for isolate_node in isolate_nodes:
                self.adjListMap[isolate_node] = [isolate_node]
                self.add_node(isolate_node)
        self.num_nodes = max_node_index
    
    
    
    
class KosarajuSCC():
    
    def __init__(self):
        self.leader = {}
    
    def init_graph(self,input_file):
        G = Graph()
        G_rev = Graph() 
        for line in open(input_file):
            tail,head=int(line.split(' ')[0]),int(line.split(' ')[1])
            G.add_edge(tail,head)
            G_rev.add_edge(head,tail)
        G.add_isolated_nodes()
        G_rev.add_isolated_nodes()
        return G,G_rev
    
    def reorder_graph(self,G,finish_time):
        G_reordered = Graph()
        G_reordered.num_nodes = G.num_nodes
        G_value = [G.adjListMap[i] if i in G.adjListMap else [] for i in range(1,G.num_nodes+1)] 
        for i in range(1,G.num_nodes+1):
            if i in G.adjListMap.keys():
                tmp = G_value[i-1]
                G_reordered.adjListMap[finish_time[i]] = [finish_time[x] for x in tmp]
        return G_reordered
    
    def Kosaraju(self,G,G_rev):
        self.leader = {}
        #Run first pass of DFS_Loop to obtain order
        finish_time = self.DFS_Loop(G_rev)
        #Reorder G using the self.finish_time
        G_rod = self.reorder_graph(G,finish_time)
        #Run second pass of DFS_Loop on reordered G.
        self.DFS_Loop(G_rod)
    
    def DFS_Loop(self,G):
        finish_time = [0 for i in range(G.num_nodes+1)] # Number of nodes processed so far (only used for 1st pass)
        t = 0 # Number of nodes processed so far (only used for 1st pass)
        s = 0 # Current source vertex (only used for 2nd pass)
        explored = set();
        for i in range(G.num_nodes,0,-1):
            if i not in explored:
                s = i
                s,t,finish_time = self.DFS(G,i,s,t,explored,finish_time)
        return finish_time
    
    def DFS(self,G,i,s,t,explored,finish_time):
        '''
        This is the function for depth first search.
        Input  graph G
               current_vertex i
               current_source_vertex s
               num_nodes_processed t
               explored_nodes explored
        Output Nothing
        '''
        explored.add(i)
        self.leader[i] = s
        if i in G.adjListMap.keys():
            for j in G.adjListMap[i]:
                if j not in explored:
                    s,t,finish_time = self.DFS(G,j,s,t,explored,finish_time)
        t += 1
        finish_time[i] = t
        return s,t,finish_time
        
    def get_top(self,num=5):
        c = collections.Counter(self.leader.values())
        res = []
        for number,count in c.most_common(num):
            res.append(count)
        while len(res)<num:
            res.append(0)
        res_str = ""
        for item in res:
            res_str+=str(item)
            res_str+=','
        return res_str[:-1]
    
class Solution():
    def run(self,input_file):
        solver = KosarajuSCC()
        G,G_rev = solver.init_graph(input_file)
        solver.Kosaraju(G,G_rev)
        res = solver.get_top(5)
        return res     

#In order to test, run the following code in command line
#python tester.py ./assignment/week5/main.py ./testCases/course2/assignment1SCC name="run"
        
#Final Solution can be obtained using the following two lines of code
sol = Solution()
res = sol.run('SCC.txt')
print(res)
#Correct answer = [434821,968,459,313,211]
        



    
    
            
    