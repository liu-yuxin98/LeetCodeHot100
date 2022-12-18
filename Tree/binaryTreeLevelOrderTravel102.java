import javax.management.ObjectName;
import java.util.*;

public class binaryTreeLevelOrderTravel102 {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        levelOrderHelper(res,root,0);
        return res;
    }

    private void levelOrderHelper(List<List<Integer>> res, TreeNode root, int height){
        if(root==null){
            return;
        }
        if(res.size()==height){
            res.add(new ArrayList<Integer>());
        }
        res.get(height).add(root.val);
        levelOrderHelper(res,root.left,height+1);
        levelOrderHelper(res,root.right,height+1);
    }
//    public List<List<Integer>> levelOrder(TreeNode root) {
//        if(root == null){
//            return new ArrayList<>();
//        }
//        Deque<List<Object>> fringe = new LinkedList<>() {};  // FIFO
//        List<List<Integer>> res = new ArrayList<>();
//        Integer curlevel = 0;
//        List<Object> firstitem = new ArrayList<>();
//        firstitem.add(curlevel);
//        firstitem.add(root);
//        fringe.add(firstitem);
//
//        List<Integer> level_res = new ArrayList<>();
//        Integer prelevel = 0;
//
//        while(true){
//            if(fringe.isEmpty()){
//                res.add(level_res);
//                break;
//            }
//           List<Object> item = fringe.remove();
//           curlevel = (Integer) item.get(0);
//           TreeNode cur_root = (TreeNode) item.get(1);
//           if(cur_root==null){
//               continue;
//           }
//           if(prelevel!=curlevel){
//                // arrives at next layer
//                res.add(level_res);
//                level_res = new ArrayList<>();
//                prelevel = curlevel;
//           }
//
//           level_res.add(cur_root.val);
//
//           item = new ArrayList<>();
//           item.add(curlevel+1);
//           item.add(cur_root.left);
//           fringe.add(new ArrayList<>(item));
//
//           item = new ArrayList<>();
//           item.add(curlevel+1);
//           item.add(cur_root.right);
//           fringe.add(new ArrayList<>(item));
//
//
//
//        }
//
//        return res;
//    }
}
