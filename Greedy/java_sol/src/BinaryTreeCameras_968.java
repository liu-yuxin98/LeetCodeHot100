import com.sun.source.tree.Tree;

public class BinaryTreeCameras_968 {
     public static class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
        }
     }


     public static int postOrderTravesal(TreeNode root){
         // return min number of cameras needed for root

         // root.val = 0 -> not covered
         // root.val = 1 -> covered but the camera is not at this root
         // root.val = 2 -> camera is at this root

         // return condition reaching leaf
         if(root ==null){
             return 0;
         }

         // return condition reaching leaf
         else if(root.left==null && root.right == null ){
             return 0;
         }

         // return condition reaching node only has right child
         else if(root.left==null && root.right != null ){
             int right_cameras = postOrderTravesal(root.right);
             if(root.right.val==0){ // right child not covered, place camera at root
                 root.val = 2;
                 return 1+right_cameras;
             } else if(root.right.val == 2){  // right child contain camera
                 root.val = 1;
                 return right_cameras;
             } else{
                 // root.right child is covered, no need to place camera here
                 return right_cameras;
             }
         }
         // return condition reaching node only has left child
         else if(root.left!=null && root.right == null ){
             int left_cameras = postOrderTravesal(root.left);
             if(root.left.val==0){ // place camera at root
                 root.val =2;
                 return 1+left_cameras;
             } else if(root.left.val == 2){
                 root.val = 1;
                 return left_cameras;
             } else{
                 // root.left child is covered, no need to place camera here
                 return left_cameras;
             }
         }
         else{
             // return condition reaching node has two child
             int left_cameras = postOrderTravesal(root.left);
             int right_cameras = postOrderTravesal(root.right);

             if(root.left.val+root.right.val >=3){
                 // no need to place camera at root and root.val=1
                 root.val = 1;
                 return left_cameras+right_cameras;
             }else if(root.left.val + root.right.val == 2){
                 // 0+2 need to place camera at root and change root.val to 2
                 if(root.left.val==0 || root.left.val ==2){
                     root.val = 2;
                     return left_cameras + right_cameras+1;
                 }
                 else{
                     // 1+1 no need to place camera at root unless root does not have parents
                     return left_cameras + right_cameras;

                 }
             } else if(root.right.val + root.left.val <= 1){
                 // 1+ 0 need to place a camera at root
                 root.val = 2;
                 return left_cameras + right_cameras + 1;
             }
         }
         System.out.println("bug");
         return -1;
     }

     public static int minCameraCover(TreeNode root) {
         // null or covered
         int camera = 0;
         camera = postOrderTravesal(root);
         if(root.left ==null &&root.right==null){
             camera += 1;
         } else if(root.left==null && root.right!=null){
             if(root.right.val==1){
                 camera += 1;
             }
         } else if(root.left!=null && root.right==null){
             if(root.left.val == 1){
                 camera += 1;
             }
         } else{
             if(root.left.val==1 && root.right.val ==1){
                 camera += 1;
             }
         }

        return camera;
     }

     public static void main(String[] args) {
         TreeNode root = new TreeNode(0);
         root.right = new TreeNode(0);
         root.left = new TreeNode(0);
         root.right.right = new TreeNode(0);
         root.right.right.right = new TreeNode(0);
//         root.right.left.left = new TreeNode(0);
//         root.left.left.left = new TreeNode(0);
//         root.left.left.left.right = new TreeNode(0);
         int cameras = minCameraCover(root);
         System.out.println(cameras);

     }

}
