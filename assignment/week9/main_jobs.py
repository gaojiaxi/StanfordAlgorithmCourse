# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 13:59:29 2019

@author: gaoji_000
"""

import pandas as pd

line_count=0
for line in open('jobs.txt'):
    if len(line.split(' '))==1:
        nums_jobs=int(line)
        W=[0 for i in range(nums_jobs)]
        L=[0 for i in range(nums_jobs)]
        Score=[0 for i in range(nums_jobs)]
    else:
        W[line_count]=int(line.split(' ')[0])
        L[line_count]=int(line.split(' ')[1])
        Score[line_count]=W[line_count]/L[line_count]
        line_count+=1
        

df=pd.DataFrame([W,L,Score])
df=df.transpose()
df.rename(columns={0:'Weight',1:'Length',2:'Score'},inplace=True)
df.sort_values(by=['Score','Weight'],inplace=True,ascending=False)
df.reset_index(drop=True,inplace=True)

C_cur=0
Cost_sum=0
for i in range(nums_jobs):
    C_cur+=df.iloc[i]['Length']
    Cost_sum+=df.iloc[i]['Weight']*C_cur

print(Cost_sum)

#69119377652

#67311454237