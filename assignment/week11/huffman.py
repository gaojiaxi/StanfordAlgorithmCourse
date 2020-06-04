# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 11:08:48 2019

@author: gaoji_000
"""

line_count=0
node_array=[]

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

for line in open('huffman.txt'):
    if line_count==0:
        num_node=int(line)
    else:
        node_array.append(TreeNode(int(line)))
    line_count+=1

def find_small(node_array):
    smallest_val=float('inf')
    smallest_node=None
    smallest_index=None
    for index,treenode in enumerate(node_array):
        if treenode.val < smallest_val:
            smallest_val=treenode.val
            smallest_node=treenode
            smallest_index=index
    return smallest_node,smallest_index

while len(node_array) > 1 :
    smallest_1st,smallest_1st_index=find_small(node_array)
    del node_array[smallest_1st_index]
    smallest_2nd,smallest_2nd_index=find_small(node_array)
    del node_array[smallest_2nd_index]
    parent_node=TreeNode(smallest_1st.val+smallest_2nd.val)
    parent_node.left=smallest_1st
    parent_node.right=smallest_2nd
    node_array.append(parent_node)

root=node_array[0]

def getHeight(root):
    if not root:
        return 0
    return 1+max(getHeight(root.left),getHeight(root.right))

max_length=getHeight(root)-1


code_set=[]
prefix=[]
def huffmanTraverse(root,prefix):
    if not root.left or not root.right:
        prefix_copy=prefix[:]
        code_set.append(prefix_copy)
    if root.left:
        prefix.append(0)
        huffmanTraverse(root.left,prefix)
        del prefix[-1]
    if root.right:
        prefix.append(1)
        huffmanTraverse(root.right,prefix)
        del prefix[-1]
        
huffmanTraverse(root,prefix)


max_length=0
min_length=1000
for item in code_set:
    if len(item)>max_length:
        max_length=len(item)
    if len(item)<min_length:
        min_length=len(item)
    
        