# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:53:25 2019

@author: gaojiaxi
"""

class Solution():
    def __init__(self):
        self.comp_nums = 0
    
    def run(self,input_file):
        left=self.run_mode(input_file,mode='left')
        middle=self.run_mode(input_file,mode='middle')
        right=self.run_mode(input_file,mode='right')
        return [left,right,middle]
    
    def run_mode(self,input_file,mode):
        self.comp_nums = 0
        nums = [int(line) for line in open(input_file) if line != '\n']
        self.QuickSort(nums,0,len(nums),mode)
        return self.comp_nums
        

    def find_median(self,a):
        median = sorted(a)[1]
        median_index=a.index(median)
        return median,median_index
        
    def ChoosePivot(self,nums,l,r,mode='left'):
        
        if mode == 'left':
            return nums[l],l
        elif mode=='right':
            return nums[r-1],r-1
        else:
            if (r-l)%2==0:
                index=[l,l+(r-l)//2-1,r-1]
                median,median_index=self.find_median([nums[index[0]],nums[index[1]],nums[index[2]]])
            else:
                index=[l,l+(r-l)//2,r-1]
                median,median_index=self.find_median([nums[index[0]],nums[index[1]],nums[index[2]]])
            return median,index[median_index]
        
    def partition(self,nums,p,l,r):
        i=l+1
        for j in range(l+1,r):
            if nums[j]<p:
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
        nums[l],nums[i-1]=nums[i-1],nums[l]
        return i-1
        
    def QuickSort(self,nums,l,r,mode):
        if r-l<=1:
            return
        p,p_index=self.ChoosePivot(nums,l,r,mode)
        nums[l],nums[p_index] = nums[p_index],nums[l]
        index=self.partition(nums,p,l,r)
        self.comp_nums+=r-l-1
        self.QuickSort(nums,l,index,mode)
        self.QuickSort(nums,index+1,r,mode)
        
#In order to test, run the following code in command line
#python tester.py ./assignment/week3/main.py ./testCases/course1/week3Quicksort name="run"

#comp_nums_left=162085
#comp_nums_right=164123
#comp_nums_middle=138382