public class LCA236 {

    private Boolean containsKey(TreeNode root, int val){
        if(root == null){
            return false;
        }
        if(root.val==val){
            return true;
        }
        return containsKey(root.left,val) || containsKey(root.right,val);

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
