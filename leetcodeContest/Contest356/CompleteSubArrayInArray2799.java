package leetcodeContest.Contest356;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class CompleteSubArrayInArray2799 {
    public static int countCompleteSubarrays(int[] nums) {
        HashMap<Integer,Integer> currentNumInSubArray = new HashMap<>();
        Set<Integer> lackNums = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            lackNums.add(nums[i]);
            currentNumInSubArray.put(nums[i],0);
        }
        int length = nums.length;
        int start = 0;
        int end = 0;
        int cnt = 0;
        while(end<length){
            // find valid subarray, move start forward
            if (lackNums.size()==0){
                cnt += length-end;
                // move start forward until not valid subarray
                currentNumInSubArray.put(nums[start], currentNumInSubArray.get(nums[start])-1);
                if(currentNumInSubArray.get(nums[start])==0){
                    lackNums.add(nums[start]);
                    end += 1;
                }
                start += 1;
            }else{
                // not find valid subarray, move end forward
                currentNumInSubArray.put(nums[end], currentNumInSubArray.get(nums[end])+1);
                lackNums.remove(nums[end]);
                if(lackNums.size()>0){
                    end += 1;
                }
            }

            
        }

        return cnt;
    }

    public static void main(String[] args) {
        int [] nums = {5,5,5,5};
        int out = countCompleteSubarrays(nums);
        System.out.println(out);

    }
}
