public class TrimBST669 {    public TreeNode trimBST(TreeNode root, int low, int high) {
    if(root==null){
        return null;
    }
    if(root.val < low){
        // cut root.left off
        root = trimBST(root.right,low,high);
    } else if(root.val > high){
        // cut root.right off
        root = trimBST(root.left,low,high);

    } else{
        root.left = trimBST(root.left,low,high);
        root.right = trimBST(root.right, low, high);
    }
    return root;
}

}
