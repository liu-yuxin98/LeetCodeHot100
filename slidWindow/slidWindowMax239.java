import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;

public class slidWindowMax239 {
    public int[] maxSlidingWindow(int[] nums, int k){
        int start = 0;
        int end = 0;

        Deque<Integer> deque = new LinkedList<>();
        List<Integer> res = new ArrayList<>();
        while(end < nums.length){
            while(deque.size() > 0 && deque.getLast()<nums[end]){
                deque.removeLast();
            }
            deque.add(nums[end]);
            if(end-start+1<k){
                end += 1;
            } else{
                res.add(deque.getFirst());
                if(deque.getFirst()==nums[start]){
                    deque.removeFirst();
                }
                start+=1;
                end += 1;
            }

        }

        int [] output = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            output[i] = res.get(i);
        }
        return output;
    }
//    public int[] maxSlidingWindow(int[] nums, int k) {
//        // TLE
//        int n = nums.length;
//        int [] dp = new int[n];
//        int max = nums[0];
//         for(int i=0;i<k;i++){
//             dp[i] = nums[i];
//             max = Math.max(nums[i],max);
//         }
//         dp[k-1] = max;
//         for(int i=k;i<n;i++){
//             if(nums[i]>=dp[i-1]){
//                 dp[i] = nums[i];
//             } else{
//                 if(nums[i-k]!=dp[i-1]){
//                     // largest not the most left
//                     dp[i] = dp[i-1];
//                 } else{
//                     // largest is the most left
////                     dp[i] = Math.max(nums[i], dp[i-2]);
//                     // this part needs improve, too slow
//                     int tempmax = nums[i-k+1];
//                     for(int j=i-k+1;j<=i;j++){
//                         tempmax = Math.max(tempmax,nums[j]);
//                     }
//                     dp[i] = tempmax;
//
//                 }
//             }
//         }
//         int [] res = new int[n-k+1];
//
//         for (int i = k-1; i < n; i++) {
//             res[i-k+1] = dp[i];
//         }
//         return res;
//
//    }
}
