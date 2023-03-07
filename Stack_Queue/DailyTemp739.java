import java.util.Arrays;
import java.util.List;
import java.util.Stack;

public class DailyTemp739 {
    public int[] dailyTemperatures(int[] temperatures) {
        int [] res = new int[temperatures.length];
        Arrays.fill(res,0);
        Stack<Integer> stack = new Stack<Integer>();
        for (int i = 0; i < temperatures.length; i++) {
            if (stack.empty()){
                stack.push(i); // push i to stack
            }else{
                //stack is not empty
                if(temperatures[stack.peek()] >= temperatures[i]){
                    stack.push(i);
                } else{

                    while (!stack.empty()){
                        if(temperatures[stack.peek()] >= temperatures[i]){
                            break;
                        } else{
                            int index = stack.pop();
                            res[index] = i-index;
                        }
                    }
                    stack.push(i);
                }

            }
        }
        return res;

    }
}
