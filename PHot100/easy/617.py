# -*- coding: utf-8 -*-
"""
Created on Mon May  3 11:37:17 2021

@author: Yuxin
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if root1 is None and root2 is None:
            return None
        else:
            root = TreeNode(0, None, None)
            if root1 is None:
                root1 = TreeNode(0)
            if root2 is None:
                root2 = TreeNode(0)
            root.val = root1.val + root2.val
            root.left = self.mergeTrees(self, root1.left, root2.left)
            root.right = self.mergeTrees(self, root1.right, root2.right)
        return root


# t12 = TreeNode(12)
# t13 = TreeNode(13)
# root1 = TreeNode(11, t12, t13)
# print(root1.val)
# print(root1.left.val)
# print(root1.right.val)
# print('------------')
# t22 = TreeNode(22)
# t23 = TreeNode(23)
# root2 = TreeNode(21, t22, t23)
# print(root2.val)
# print(root2.left.val)
# print(root2.right.val)
# print('------------')
# s = Solution
# root = s.mergeTrees(s, root1, root2)
# print(root.val)
# print(root.left.val)
# print(root.right.val)
# print('end')

