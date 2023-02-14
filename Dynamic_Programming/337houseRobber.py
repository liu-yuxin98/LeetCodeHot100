
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        valuedict = dict()
        res = self.robhelper(root, valuedict)
        return res

    def robhelper(self, root, valuedict):
        if root is None:
            return 0
        if root in valuedict:
            return valuedict[root]
        elif root.left is None and root.right is None:
            valuedict[root] = root.val
            return root.val
        elif root.left is None:
            notSelectRoot = self.robhelper(root.right, valuedict)
            selectRoot = root.val + \
                self.robhelper(root.right.left, valuedict) + \
                self.robhelper(root.right.right, valuedict)
        elif root.right is None:
            notSelectRoot = self.robhelper(root.left, valuedict)
            selectRoot = root.val + \
                self.robhelper(root.left.left, valuedict) + \
                self.robhelper(root.left.right, valuedict)
        else:
            notSelectRoot = self.robhelper(
                root.left, valuedict)+self.robhelper(root.right, valuedict)
            selectRoot = root.val + self.robhelper(root.right.left, valuedict)+self.robhelper(
                root.right.right, valuedict)+self.robhelper(root.left.left, valuedict)+self.robhelper(root.left.right, valuedict)
        valuedict[root] = max(notSelectRoot, selectRoot)
        return valuedict[root]


s = Solution()

root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)

print(s.rob(root))
