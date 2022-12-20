import java.util.*;

public class findModeInBST501 {




//    HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
//
//    private void helper(TreeNode root){
//        if(root == null){
//            return;
//        }
//        if(map.containsKey(root.val)){
//            map.put(root.val, map.get(root.val)+1);
//        }    else{
//            map.put(root.val, 1);
//        }
//        helper(root.left);
//        helper(root.right);
//    }
//
//    public int[] findMode(TreeNode root) {
//        helper(root);
//        int max = Integer.MIN_VALUE;
//        List<Integer> temp = new ArrayList<Integer>();
//        for(HashMap.Entry< Integer, Integer> set: map.entrySet()){
//            System.out.println(set.getValue());
//                max = Math.max(max, set.getValue());
//        }
//        for(HashMap.Entry< Integer, Integer> set: map.entrySet()){
//            if(set.getValue() == max){
//                temp.add(set.getKey());
//            }
//        }
//        System.out.println(max);
//        int [] res = new int[temp.size()];
//        for(int i = 0; i < temp.size(); i++){
//            res[i] = temp.get(i);
//        }
//        return res;
//
//    }
}
