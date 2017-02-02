'''
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following ordering properties:

The  value of every node in a node's left subtree is less than the data value of that node.
The  value of every node in a node's right subtree is greater than the data value of that node.
Given the root node of a binary tree, can you determine if it's also a binary search tree?

Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must return a boolean denoting whether or not the binary tree is a binary search tree. You may have to write one or more helper functions to complete this challenge.

Note: We do not consider a binary tree to be a binary search tree if it contains duplicate values.

'''

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def is_bst_satisfied(n,min_val,max_val):
    if n.right is None and n.right is None:
        if n.data <= max_val and n.data >= min_val:
            return True
        else:
            return False
    else:
        return is_bst_satisfied(n.left,min_val,n.data-1) and is_bst_satisfied(n.right,n.data+1,max_val)
def check_binary_search_tree_(root):
    return is_bst_satisfied(root,-10000,20000)
