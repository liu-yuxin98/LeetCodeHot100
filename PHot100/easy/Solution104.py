class Solution104:
    def maxDepth(self, root):
        if root ==None:
            return 0
        else:
            return self.finddepth(root,0)

    def finddepth(self,root,n):
        if root == None:
            return n
        else:
            return max(self.finddepth(root.left,n+1),self.finddepth(root.right,n+1))

