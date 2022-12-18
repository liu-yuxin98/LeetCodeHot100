public class countCompleteTreeNode222 {
    private int getDepth(TreeNode root){
        TreeNode temp = root;
        int depth = 0;
        while(temp!=null){
            depth += 1;
            temp = temp.left;
        }
        return depth;
    }

    private int countLastLayerNodes(TreeNode root, int curlayer, int maxlayer){
        if(root == null){
            return 0;
        }
        if(curlayer==maxlayer){
            return 1;
        }
        Integer left = countLastLayerNodes(root.left, curlayer+1,maxlayer);
        Integer right = countLastLayerNodes(root.right,curlayer+1,maxlayer);
        return  left+right;
    }
    public int countNodes(TreeNode root) {
        int depth = getDepth(root);
        int cnt = 0;
        int numLastlayer = countLastLayerNodes(root,1,depth);
        System.out.println(depth);
        System.out.println(numLastlayer);
        for(int i=0;i<depth-1;i++){
            cnt += Math.pow(2,i);
        }
        cnt += numLastlayer;
        return cnt;
    }
}
