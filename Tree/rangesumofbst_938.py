class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rangeSumBST(root: list[TreeNode], low: int, high: int) -> int:

    def tree_travel(root, low, high):
        sum = 0
        left = 0
        right = 0
        if root is None:
            return 0
        if root.val >= low and root.val <= high:
            sum += root.val
            left = tree_travel(root.left, low, high)
            right = tree_travel(root.right, low, high)
        elif root.val < low:
            right = tree_travel(root.right, low, high)
        else:
            left = tree_travel(root.left, low, high)

        sum += left+right
        return sum

    sum = tree_travel(root, low, high)
    return sum
