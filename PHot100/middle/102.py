# -*- coding: utf-8 -*-
"""
Created on Thu May  6 22:21:28 2021

@author: yuxin
"""

def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    levels = []

    def helper_level_order(root, level):
        if len(levels) == level:
            levels.append([])
        levels[level].append(root.val)
        if root.left is not None:
            helper_level_order(root.left, level+1)
        if root.right is not None:
            helper_level_order(root.right, level+1)
    if root is None:
        return levels
    else:
        helper_level_order(root, 0)
        return levels

        
        



 