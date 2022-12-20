public class lowestCommonAncestorOfBST235 {

    private Boolean containsKey(TreeNode root, int val){
        TreeNode temp = root;
        while (true){
            if(temp==null){
                return false;
            }
            if(temp.val==val){
                return true;
            }
            if(temp.val>val){
                temp = temp.left;
            } else{
                temp = temp.right;
            }
        }
    }
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if(root==null){
            return null;
        }

        TreeNode leftAncestor = lowestCommonAncestor(root.left,p,q);
        if(leftAncestor != null){
            return leftAncestor;
        }
        TreeNode rightAncestor = lowestCommonAncestor(root.right,p,q);
        if(rightAncestor != null){
            return rightAncestor;
        }

        if(containsKey(root,p.val) && containsKey(root,q.val)){
            return root;
        }
        return null;
    }
}
