class TreeNode:
    def __init__(self, val, left, right) -> None:
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(0, None, None)


def preTraversal(root: TreeNode):
    # mid,left,right
    if root is None:
        return
    print(root.val)
    preTraversal(root.left)
    preTraversal(root.right)


def inTraversal(root: TreeNode):
    # left,mid, right
    if root is None:
        return
    inTraversal(root.left)
    print(root.val)
    inTraversal(root.right)


def postTraversal(root: TreeNode):
    # left, right,mid
    if root is None:
        return
    postTraversal(root.left)
    postTraversal(root.right)
    print(root.val)


# deep first
