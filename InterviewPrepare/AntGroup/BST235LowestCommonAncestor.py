class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return root
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

    # !!!! 注意这是BST
        # nodeDict = dict()

        # def nodeInroot(root, p):
        #     # if p in tree with root as root return True
        #     if root is None:
        #         return False
        #     if p == root:
        #         return True
        #     else:
        #         if root.left in nodeDict and p in nodeDict[root.left]:
        #             return True
        #         else:
        #             inLeft = nodeInroot(root.left, p)
        #             if inLeft:
        #                 if root.left not in nodeDict:
        #                     nodeDict[root.left] = set()
        #                 nodeDict[root.left].add(p)
        #                 return True
        #         if root.right in nodeDict and p in nodeDict[root.right]:
        #             return True
        #         else:
        #             inRight = nodeInroot(root.right, p)
        #             if inRight:
        #                 if root.right not in nodeDict:
        #                     nodeDict[root.right] = set()
        #                 nodeDict[root.right].add(p)
        #                 return True
        #         return False

        # def lowSameRoot(pre, root, p, q):
        #     if nodeInroot(root, p) == False or nodeInroot(root, q) == False:
        #         return pre
        #     else:
        #         pInleft = nodeInroot(root.left, p)
        #         qInleft = nodeInroot(root.left, q)
        #         if pInleft and qInleft:
        #             return lowSameRoot(root.left, root.left, p, q)
        #         pInright = nodeInroot(root.right, p)
        #         qInright = nodeInroot(root.right, q)
        #         if pInright and qInright:
        #             return lowSameRoot(root.right, root.right, p, q)
        #         return pre

        # return lowSameRoot(root, root, p, q)


tree = TreeNode(6)
tree.left = TreeNode(2)
tree.right = TreeNode(3)


sol = Solution()
res = sol.lowestCommonAncestor(tree, tree.left, tree.right)
print(res.val)
