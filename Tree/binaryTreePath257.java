import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

public class binaryTreePath257 {

    List<String> res = new ArrayList<>();
    List<String> path = new LinkedList<>();


    private void getAllPath(TreeNode root, List<String> path){
        if(root==null){
            path.add("");
            return;
        }
        if(root.left == null && root.right == null){
            path.add(String.valueOf(root.val));
            res.add(String.join("->", path));
            return;
        }
        path.add(String.valueOf(root.val));
        getAllPath(root.left,path);
        path.remove(path.size() - 1);
        getAllPath(root.right, path);
        path.remove(path.size() - 1);
    }
    public List<String> binaryTreePaths(TreeNode root) {
        res = new ArrayList<>();
        path = new LinkedList<>();
        getAllPath(root,path);
        return res;
    }
}
