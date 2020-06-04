# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:21:36 2019

@author: gaoji_000
"""

import pandas as pd

columns = ['Node1','Node2', 'Distance']
graph_df=pd.DataFrame(columns=columns)

line_count=0
for line in open('clustering1.txt'):
    if line != '\n' and len(line.split(' '))==1:
        num_node=int(line)
    elif line != '\n':
        graph_df = graph_df.append(pd.Series([int(line.split(' ')[0]),int(line.split(' ')[1]),int(line.split(' ')[2])], index=graph_df.columns), ignore_index=True)

graph_df.sort_values(by=['Distance'],inplace=True,ascending=True)

columns = ['Node','Leader', 'LeaderSize']
Union_find_df=pd.DataFrame(columns=columns)
for i in range(1,num_node+1):
    Union_find_df = Union_find_df.append(pd.Series([i,i,1], index=Union_find_df.columns), ignore_index=True)
Union_find_df.set_index(keys='Node',inplace=True)

for index in range(len(graph_df)):
    curNode1=graph_df.iloc[index]['Node1']
    curNode2=graph_df.iloc[index]['Node2']
    curNode1_size=Union_find_df.loc[curNode1]['LeaderSize']
    curNode2_size=Union_find_df.loc[curNode2]['LeaderSize']
    if Union_find_df.loc[curNode1]['Leader'] != Union_find_df.loc[curNode2]['Leader']:
        if Union_find_df.loc[curNode1]['LeaderSize'] < Union_find_df.loc[curNode2]['LeaderSize']:
            condition_index=Union_find_df[Union_find_df['Leader']==Union_find_df.loc[curNode1]['Leader']].index
            Union_find_df.loc[condition_index,'Leader']=Union_find_df.loc[curNode2]['Leader']
            Union_find_df.loc[condition_index,'LeaderSize']=curNode1_size+curNode2_size
            condition_index=Union_find_df[Union_find_df['Leader']==Union_find_df.loc[curNode2]['Leader']].index
            Union_find_df.loc[condition_index,'LeaderSize']=curNode1_size+curNode2_size
        else:
            condition_index=Union_find_df[Union_find_df['Leader']==Union_find_df.loc[curNode2]['Leader']].index
            Union_find_df.loc[condition_index,'Leader']=Union_find_df.loc[curNode1]['Leader']
            Union_find_df.loc[condition_index,'LeaderSize']=curNode1_size+curNode2_size
            condition_index=Union_find_df[Union_find_df['Leader']==Union_find_df.loc[curNode1]['Leader']].index
            Union_find_df.loc[condition_index,'LeaderSize']=curNode1_size+curNode2_size
        
    if len(Union_find_df['Leader'].value_counts())==4:
        break

while index < len(graph_df):
    curNode1=graph_df.iloc[index]['Node1']
    curNode2=graph_df.iloc[index]['Node2']
    if Union_find_df.loc[curNode1]['Leader'] != Union_find_df.loc[curNode2]['Leader']:
        result=graph_df.iloc[index]['Distance']
        break
    index+=1


#df.reset_index(drop=True,inplace=True)