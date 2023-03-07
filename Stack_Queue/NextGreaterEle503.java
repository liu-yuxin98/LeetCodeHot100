import java.util.Arrays;
import java.util.Stack;

public class NextGreaterEle503 {
    public int[] nextGreaterElements(int[] nums) {
        int [] res = new int[nums.length];
        Arrays.fill(res, -1);
        Stack<Integer> stack = new Stack<Integer>();
        int max =  nums[0];
        for (int i = 0; i < nums.length; i++) {
            max = Math.max(max,nums[i]);
            if(stack.empty()){
                stack.push(i);
            }   else{
                if(nums[stack.peek()] >=nums[i]){
                    stack.push(i);
                } else{
                    while (!stack.empty()){
                        if(nums[stack.peek()] >=nums[i]){
                            break;
                        } else {
                            int index = stack.pop();
                            res[index] = nums[i];
                        }
                    }
                    stack.push(i);
                }
            }
        }

        // deal with remaining element in stack
        int i = 0;
        while(stack.size() >1){
            int index = stack.peek();
            if(nums[index] == max){
                break;
            }
            if(nums[i]>nums[index]){
                res[index] = nums[i];
                stack.pop();
            }else{
                i += 1;
            }

        }

        return res;
    }
}
