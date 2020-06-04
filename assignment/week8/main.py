# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:27:50 2019

@author: gaoji_000
"""
#naive solution: time complexity is O(20000n) 
#nums_dict={}
#for line in open('2sum.txt'):
#    nums=int(line)
#    nums_dict[nums]=''
#
#nums_target=0
#for target in range(-10000,10001,1):
#    for key in nums_dict.keys():
#        if target - key in nums_dict.keys() and key!= target-key:
#            nums_target+=1
#            break

#advanced solution:

nums_list=[]
nums_target=0
for line in open('2sum.txt'):
    num=int(line)
    nums_list.append(num)
nums_list=sorted(nums_list)
i=0
j=len(nums_list)-1
solution_dict={}
while i<j:
    cur=nums_list[i]+nums_list[j]
    if cur>10000:
        j-=1
    elif cur<-10000:
        i+=1
    else:
        if cur not in solution_dict.keys():
            solution_dict[cur]=''
            nums_target+=1
        i+=1