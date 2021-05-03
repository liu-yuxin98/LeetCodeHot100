# -*- coding: utf-8 -*-
"""
Created on Mon May  3 12:13:35 2021

@author: liu yuxin
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root is None:
            return None
        root.left = self.invertTree(self, root.left)
        root.right = self.invertTree(self, root.right)
        root.left, root.right = root.right, root.left
        return root


# t12 = TreeNode(12)
# t13 = TreeNode(13)
# root1 = TreeNode(11, t12, t13)
# print(root1.val)
# print(root1.left.val)
# print(root1.right.val)
# print('------------')
# s = Solution
# root1 = s.invertTree(s, root1)
# print(root1.val)
# print(root1.left.val)
# print(root1.right.val)
# print('-----end-------')
