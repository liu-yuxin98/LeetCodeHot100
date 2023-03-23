class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        left = self.invertTree(root.right)
        right = self.invertTree(root.left)
        root.left = left
        root.right = right
        return root
