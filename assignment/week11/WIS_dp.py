# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:27:06 2019

@author: gaoji_000
"""

line_count=0
node_weight=[0]
Solution=[]

for line in open('mwis_small.txt'):
    if line_count==0:
        num_node=int(line)
        A=[0 for i in range(num_node+1)]
    elif line_count==1:
        A[0]=0
        A[1]=int(line)
        node_weight.append(int(line))
    else:
        A[line_count]=max(A[line_count-1],A[line_count-2]+int(line))
        node_weight.append(int(line))
    line_count+=1

i=num_node

while i > 0:
    if A[i-1] >= A[i-2]+node_weight[i]:
        i-=1
    else:
        Solution.append(i)
        i-=2


#check_set=[1, 2, 3, 4, 17, 117, 517,997]
#
#for item in check_set:
#    print(item in Solution)
    
    
total=0
    
for item in Solution:
    total+=node_weight[item]