import java.util.Arrays;
import java.util.OptionalInt;
import java.util.stream.IntStream;

public class constructBSTfromInToPost106 {

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if(postorder.length==0){
            return null;
        }
        if(postorder.length == 1){
            return new TreeNode(postorder[0]);
        }
        TreeNode root = new TreeNode();
        root.val = postorder[postorder.length-1];
        System.out.println(root.val);

        int index = IntStream.range(0,inorder.length).filter(i->inorder[i]== root.val).findFirst().orElse(-1);
        int [] inorderLeft = Arrays.copyOfRange(inorder, 0,index);
        int [] inorderRight = Arrays.copyOfRange(inorder, index + 1, inorder.length);
        int numInLeft = inorderLeft.length;
        int [] postorderLeft = Arrays.copyOfRange(postorder,0, numInLeft);
        int [] postorderRight = Arrays.copyOfRange(postorder, numInLeft, postorder.length-1);
        root.left = buildTree(inorderLeft,postorderLeft);
        root.right = buildTree(inorderRight,postorderRight);
        return  root;
    }
}
