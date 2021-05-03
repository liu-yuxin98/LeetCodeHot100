class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution101:
    def isSymmetric(self, root):
        return self.checkSymmetic(root.left,root.right)

    def checkSymmetic(self,left,right):
        if left == None and right == None:
            return True
        elif left == None or right == None:
            return False
        else:
            if left.val != right.val:
                return False
            else:
                return self.checkSymmetic(left.left, right.right) and self.checkSymmetic(left.right, right.left)









