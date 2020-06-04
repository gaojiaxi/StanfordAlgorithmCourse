# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 11:57:39 2020

@author: gaoji_000
"""

import math

class Solution():

    def multiply_helper(self,x,y,n):
        if n==1:
            return x*y
        
        a=x//(10**(n//2))
        b=x%(10**(n//2))
        c=y//(10**(n//2))
        d=y%(10**(n//2))
        
        ac=self.multiply_helper(a,c,n//2)
        ad=self.multiply_helper(a,d,n//2)
        bc=self.multiply_helper(b,c,n//2)
        bd=self.multiply_helper(b,d,n//2)
        
        return ac*(10**((n//2)*2))+(ad+bc)*(10**(n//2))+bd
    
    def multiply(self,input_file):
        
        f = open(input_file,"r",encoding="utf-8")
        
        [x,y]=[int(line) for line in f.readlines()]
        
        f.close()
        
        n = math.floor(math.log10(x)+1)
        
        return self.multiply_helper(x,y,n)

#In order to test, run the following code in command line
#python tester.py ./assignment/week1/main.py ./testCases/course1/week1Multiplication name="multiply"