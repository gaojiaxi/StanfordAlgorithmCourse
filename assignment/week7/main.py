# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:51:45 2019

@author: gaoji_000
"""
import numpy
cur_median=0
from heapq import *
max_heap=[]
min_heap=[]
median_sum=0
nums_list=[]
for line in open('Median.txt'):
    item=0
    nums=int(line)
    nums_list.append(nums)
    if nums>cur_median:
        heappush(min_heap,nums)
    else:
        heappush(max_heap,-nums)
    if abs(len(max_heap)-len(min_heap))>1:
        if len(max_heap)-len(min_heap)>1:
            item_max=heappop(max_heap)
            item=-item_max
            heappush(min_heap,item)
        else:
            item_min=heappop(min_heap)
            item=item_min
            heappush(max_heap,-item)
    if len(max_heap)-len(min_heap)>=0:
        cur_median=-max_heap[0]
    else:
        cur_median=min_heap[0]
    median_sum+=cur_median
    
    nums_list=sorted(nums_list)
    if len(nums_list)%2 != 0:
        median=nums_list[len(nums_list)//2]
    else:
        median=nums_list[len(nums_list)//2-1]
    assert(cur_median==median)

result=median_sum % 10000