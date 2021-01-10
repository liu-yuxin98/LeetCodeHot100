/*
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

EXAMPLE:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
* */

import java.util.*;

public class Solution1 {
    /* solution1.1 */
    private static  int[] twoSum(int[] nums, int target) {

        Set<Integer> vaules = new HashSet<>();
        List<Integer> res = new ArrayList<>();
        /* create map to store the key-value pairs of (number,target-number)*/
        Map<Integer,Integer> TargetMinus = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            res.add(nums[i]);
            vaules.add(nums[i]);
            TargetMinus.put(nums[i],target-nums[i]);
        }
        for(int i=0;i< nums.length-1;i++){
            /* if TargetMinus.get(keys) in values set */
            int difference = TargetMinus.get(nums[i]);
            if(vaules.contains(difference)){
                /* get the index of the TargetMinus.get(nums[i]) */
                for(int j=i+1;j< nums.length;j++){
                    if(nums[j] == difference){
                        /* find the answer*/
                        int[] result = new int[2];
                        result[0]  = i;
                        result[1] = j;
                        return result;
                    }
                }
            }
        }
        return null;

    }

    public static void main(String[] args){
        int[] nums = new int[]{3,3};
        int target = 6;
        int[] res = Solution1.twoSum(nums,target);

    }


}
