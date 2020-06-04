# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:14:30 2019

@author: gaojiaxi
"""

class Solution():
    
    def __init__(self):
        self.nums_inverse=0
    
    def run(self,input_file):
        nums = [int(line.rstrip('\n')) for line in open(input_file)]
        self.nums_inverse=0
        self.mergesort(nums)
        return self.nums_inverse
    

    def mergesort(self,nums):
            
        if len(nums)<=1:
            return nums
        l=0
        r=len(nums)
        mid=l+(r-l)//2
        
        left=self.mergesort(nums[:mid])
        right=self.mergesort(nums[mid:])
        ret=self.merge(left,right)
        return ret
    
    def merge(self,L,R):
        ret=[]
        i=0
        j=0
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                ret.append(L[i])
                i+=1
            else:
                ret.append(R[j])
                self.nums_inverse+=len(L)-i
                j+=1
        while i<len(L):
            ret.append(L[i])
            i+=1
        while j<len(R):
            ret.append(R[j])
            j+=1
        return ret
    


#In order to test, run the following code in command line
#python tester.py ./assignment/week2/main.py ./testCases/course1/week2Inversions name="run"