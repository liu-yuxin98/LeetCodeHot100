import java.util.Stack;

public class TrappingRainWater42 {
//    public int trap(int[] height) {
//        int res = 0;
//        Stack<Integer> stack = new Stack<Integer>();
//        int max_index = 0;
//        for (int i = 0; i < height.length; i++) {
//            if(height[i]>height[max_index]){
//                max_index = i;
//            }
//        }
//        // left part
//        for (int i = 0; i <= max_index; i++) {
//            if(stack.empty()){
//                stack.push(i);
//            } else{
//                if(height[i]>= height[stack.peek()]){
//                    int left_index = stack.pop();
//                    for (int j = left_index; j < i; j++) {
//                        res += Math.max(height[left_index]-height[j],0);
//                    }
//                    stack.push(i);
//                }
//            }
//        }
//        stack.pop();
//        //right part
//        for (int i = height.length - 1; i >= max_index; i--) {
//            if(stack.empty()){
//                stack.push(i);
//            }else{
//                if(height[i]>=height[stack.peek()]){
//                    int right_index = stack.pop();
//                    for(int j=right_index;j>i;j--){
//                        res += Math.max(height[right_index]-height[j],0 );
//                    }
//                    stack.push(i);
//                }
//            }
//        }
//        return res;
//    }
    public int trap(int[] height) {
        // TIME O(N) SPACE O(N)
        if(height.length<=2){
            return 0;
        }
        int res = 0;
        Stack<Integer> stack = new Stack<>(); // stack, smaller item at top, big item at bottom
        stack.push(0);
        for (int i = 1; i < height.length; i++) {
            if( height[stack.peek()]>height[i]){
                stack.push(i);
            } else if(height[stack.peek()]== height[i]){
                stack.pop();
                stack.push(i);
            }  else{
                while(!stack.empty() && height[i]>height[stack.peek()]) {
                    int mid = stack.peek();
                    stack.pop();
                    if (!stack.empty()) {
                        int w = i - stack.peek() -1;
                        int h = Math.min(height[stack.peek()],height[i]) -height[mid] ;
                        res += h*w;
                    }
                }
                stack.push(i);
            }
        }
        return res;
    }

}
