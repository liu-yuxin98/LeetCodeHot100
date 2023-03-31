class Solution:
    def IsBalanced_Solution(self, pRoot) -> bool:
        import math
        if pRoot is None:
            return True
        elif math.fabs(self.Height(pRoot.left, 0)-self.Height(pRoot.right, 0)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    def Height(self, root, h):
        if root is None:
            return h
        return max(self.Height(root.left, h+1), self.Height(root.right, h+1))
