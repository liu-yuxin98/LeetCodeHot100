# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:12:21 2021

@author: Yuxin
"""

def inorderTraversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    nodelist = []
    if root is None:
        return nodelist
    left = inorderTraversal(root.left)
    nodelist.extend(left)
    nodelist.append(root.val)
    right = inorderTraversal(root.right)
    nodelist.extend(right)
    return nodelist
    

