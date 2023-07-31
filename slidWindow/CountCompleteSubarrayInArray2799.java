package slidWindow;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Set;

public class CountCompleteSubarrayInArray2799 {
    public static int countCompleteSubarrays(int[] nums) {
        HashMap<Integer,Integer> numContained = new HashMap<Integer, Integer>();
        int numOfItems = 0;
        Set<Integer> unqiues = new HashSet<Integer>();
        for(int num:nums){
            unqiues.add(num);
        }
        numOfItems = unqiues.size();
        int start = 0;
        int end = 0;
        int cnt =0;

        while( end<nums.length){
            // add nums[end] to map
            if(numContained.containsKey(nums[end])) {
                numContained.put(nums[end], numContained.get(nums[end]) + 1);
            }else{
                numContained.put(nums[end], 1);
            }
            // if not valid move end forward
            if(numContained.size()<numOfItems){
                end ++;
            }else{
                //if valid move start forward until invalid
                while(start<nums.length && numContained.size()==numOfItems) {
                    cnt += nums.length - end;
                    if (numContained.get(nums[start]) == 1) {
                        numContained.remove(nums[start]);
                    } else {
                        numContained.put(nums[start], numContained.get(nums[start]) - 1);
                    }
                    start++;
                }
                end ++;

            }

        }

        return cnt;
    }

    public static void main(String[] args) {
        int [] nums = {1, 1,1,1};
        System.out.println(countCompleteSubarrays(nums));

    }
}
