# -*- coding: utf-8 -*-
"""
Created on Mon May  3 21:51:19 2021

@author: Liu yuxin
"""


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1

        def depth(node):
            # to the end return 0
            if not node:
                return 0
            L = depth(node.left)
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1

    #     if root is None:
    #         return 0
    #     max_now = self.depth(root.left) + self.depth(root.right)
    #     maxlen = max(max_now, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    #     return maxlen

    # def depth(self, root):
    #     depth = 0
    #     if root is None:
    #         return 0
    #     depth = 1 + max(self.depth(root.left), self.depth(root.right))
    #     return depth


