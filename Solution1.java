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

import org.junit.Test;

import java.util.*;

public class Solution1 {
    /* solution1.1 */
    private static  int[] twoSum(int[] nums, int target) {
        /* create a hashmap for nums[i] and its index    (nums[i],i) */
        HashMap<Integer,Integer> hashtable = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            /* find the answer*/
            if(hashtable.containsKey(target-nums[i])){
                int[] res = new int[]{i,hashtable.get(target-nums[i])};
                return res;
            }
            /* store key-value in map*/
            hashtable.put(nums[i],i);
        }
        return new int[0];

    }

    /* test esveral cases*/
    public static void main(String[] args){
        int[] nums = new int[]{3,3};
        int target = 6;
        int[] res = Solution1.twoSum(nums,target);
    }


}
