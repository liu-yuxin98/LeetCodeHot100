public class seachInBST700 {
    public TreeNode searchBST(TreeNode root, int val) {
        TreeNode temp = root;
        while(true){
            if(temp == null){
                return null;
            }
            if(temp.val==val){
                return temp;
            }
            if(temp.val > val){
                temp = temp.left;
            }
            else{
                temp = temp.right;
            }

        }

    }
}
