import java.util.Arrays;
import java.util.Stack;

public class LargestRectangle84 {
    public int largestRectangleArea(int[] heights) {
        int max = heights[0];
        Stack<Integer> stack = new Stack<>(); // small value at bottom
        int [] smallerInLeft = new int[heights.length];
        int [] smallerInRight = new int[heights.length];
        smallerInLeft[0] = -1;
        smallerInRight[heights.length-1] = heights.length;
        stack.push(0);
        for (int i = 1; i < heights.length; i++) {
            if(heights[i] >= heights[stack.peek()]){
                stack.push(i);
            } else{
              while(!stack.empty() && heights[stack.peek()]>= heights[i]){
                    int index = stack.pop();
                    if(stack.empty()){
                      smallerInLeft[index] = -1;
                    } else{
                        int smallerLeft = stack.peek();
                        smallerInLeft[index] = smallerLeft;
                    }
              }
              stack.push(i);
            }
            System.out.println(stack);
        }
        while (!stack.empty()){
            int index = stack.pop();
            if(stack.empty()){
                smallerInLeft[index] = -1;
            } else{
                smallerInLeft[index] = stack.peek();
            }
        }

        stack = new Stack<>();
        stack.push(heights.length-1);
        for (int i = heights.length - 2; i >=0; i--) {
            if(heights[i] > heights[stack.peek()]){
                stack.push(i);
            } else{
                while(!stack.empty() && heights[stack.peek()]>= heights[i]){
                    int index = stack.pop();
                    if(stack.empty()){
                        smallerInRight[index] = heights.length;
                    } else{
                        int smallerRight = stack.peek();
                        smallerInRight[index] = smallerRight;
                    }
                }
                stack.push(i);
            }
        }

        while (!stack.empty()){
            int index = stack.pop();
            if(stack.empty()){
                smallerInRight[index] = heights.length;
            } else{
                smallerInRight[index] = stack.peek();
            }
        }

        System.out.println(Arrays.toString(smallerInLeft));
        System.out.println(Arrays.toString(smallerInRight));
        for (int i = 0; i < heights.length; i++) {
            max = Math.max(max, heights[i]*(smallerInRight[i]-smallerInLeft[i]-1));
        }

        return max;
    }
}
