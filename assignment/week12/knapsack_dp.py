# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:27:00 2019

@author: gaojiaxi
"""



class Solution():
    def read_file(self,input_file):
        line_count = 0
        val = [0]
        W = [0]
        for line in open(input_file):
            if line_count == 0:
                max_weight=int(line.split(' ')[0])
                num_nodes=int(line.split(' ')[1])
            else:
                val.append(int(line.split(' ')[0]))
                W.append(int(line.split(' ')[1]))
            line_count += 1
        return W,val,max_weight,num_nodes
    def Knapsack(self,input_file):
        W,val,max_weight,num_nodes = self.read_file(input_file)
        A = [[0 for _ in range(max_weight+1)]for _ in range(num_nodes+1)]
        for i in range(1,num_nodes+1):
            for x in range(max_weight+1):
                if x - W[i] < 0:
                    A[i][x] = A[i-1][x]
                else:
                    A[i][x] = max(A[i-1][x],A[i-1][x-W[i]]+val[i])
        return A[num_nodes][max_weight]
    
    def Knapsack_efficient(self,input_file):
        W,val,max_weight,num_nodes = self.read_file(input_file)
        A = [[0 for _ in range(max_weight+1)]for _ in range(2)]
        for i in range(1,num_nodes+1):
            for x in range(max_weight+1):
                if x - W[i] < 0:
                    A[1][x] = A[0][x]
                else:
                    A[1][x] = max(A[0][x],A[0][x-W[i]]+val[i])
            A[0] = A[1][:]
            
        return A[1][max_weight]
    
    def run(self,input_file):
        res = self.Knapsack_efficient(input_file)
        return res
    
    
#In order to test, run the following code in command line
#python tester.py ./assignment/week12/knapsack_dp.py ./testCases/course3/assignment4Knapsack_simple name="run"

#Final Solution can be obtained using the following two lines of code
#sol = Solution()
#res_effi = sol.run('knapsack1.txt')
#Correct answer = 2493893

        