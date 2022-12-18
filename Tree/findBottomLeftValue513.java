import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class findBottomLeftValue513 {

    Integer res ;
    public int maxDepthHelper(TreeNode root, Integer depth){
        if(root==null){
            return depth;
        }
        return Math.max(maxDepthHelper(root.left, depth+1), maxDepthHelper(root.right, depth+1));
    }


    private boolean bottomLeftHelper(TreeNode root, Integer depth, Integer maxDepth){

        if(root == null) {
            return false;
        }
        if(Objects.equals(depth, maxDepth-1)){
            res = root.val;
            return true;
        }
        if (bottomLeftHelper(root.left,depth + 1,maxDepth)){
            return true;
        } else {
            if(bottomLeftHelper(root.right,depth + 1,maxDepth)){
                return true;
            }}
        return false;
    }

    public int findBottomLeftValue(TreeNode root) {
        int maxDepth = maxDepthHelper(root,0);
        bottomLeftHelper(root,0,maxDepth);
        return res;
    }
}
