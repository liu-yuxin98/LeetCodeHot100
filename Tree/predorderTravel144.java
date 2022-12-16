import java.util.ArrayList;
import java.util.List;

public class predorderTravel144 {

    private List<Integer> IntravelHelper(TreeNode root){
        List<Integer> path = new ArrayList<Integer>();
        if(root == null){
            return new ArrayList<Integer>();
        }
        List<Integer> left = IntravelHelper(root.left);
        List<Integer> right = IntravelHelper(root.right);
        path.addAll(left);
        path.add(root.val);
        path.addAll(right);
        return path;
    }

    private List<Integer> posttravelHelper(TreeNode root){
        List<Integer> path = new ArrayList<Integer>();
        if(root == null){
            return new ArrayList<Integer>();
        }
        List<Integer> left = posttravelHelper(root.left);
        List<Integer> right = posttravelHelper(root.right);
        path.addAll(left);
        path.addAll(right);
        path.add(root.val);
        return path;
    }
    private List<Integer> pretravelHelper(TreeNode root){
        List<Integer> path = new ArrayList<Integer>();
        if(root == null){
            return new ArrayList<Integer>();
        }
        path.add(root.val);
        List<Integer> left = pretravelHelper(root.left);
        List<Integer> right = pretravelHelper(root.right);
        path.addAll(left);
        path.addAll(right);
        return path;
    }

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> path = posttravelHelper(root);
        return path;
    }

}
