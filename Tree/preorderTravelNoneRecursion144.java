import java.util.ArrayList;
import java.util.Deque;
import java.util.List;
import java.util.Stack;

public class preorderTravelNoneRecursion144 {
    // using none recursion solution to solve tree traversal
    public List<Integer> preorderTraversal(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> res = new ArrayList<Integer>();
        stack.push(root);

        while(true){
            if(stack.isEmpty()){
                break;
            }
            TreeNode cur_root = stack.pop();
            if(cur_root==null){
                continue;
            }
            res.add(cur_root.val);
            stack.push(cur_root.right);
            stack.push(cur_root.left);
        }
        return res;
    }

}
