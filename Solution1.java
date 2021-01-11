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
import static org.junit.Assert.*;
import java.util.*;

public class Solution1 {
    /* solution1.1 */
    private static  int[] twoSum(int[] nums, int target) {
        /* create a hashmap for nums[i] and its index    (nums[i],i) */
        HashMap<Integer,Integer> hashtable = new HashMap<>();
        for(int i=0;i<nums.length;i++){
            /* find the answer*/
            if(hashtable.containsKey(target-nums[i])){
                int[] res = new int[]{hashtable.get(target-nums[i]),i};
                return res;
            }
            /* store key-value in map*/
            hashtable.put(nums[i],i);
        }
        return new int[0];

    }

    /* test esveral cases*/
    @Test
    public void Testcases(){
        /* basic case */
        int[] nums = new int[]{2,7,11,15};
        int target = 9;
        int[] actual0 = Solution1.twoSum(nums,target);
        int[] expeted0 = new int[]{0,1};
        assertArrayEquals(actual0,expeted0);


        /* case one  [3,3] 6  */
        nums = new int[]{3,3};
        target = 6;
        int[] actual1 = Solution1.twoSum(nums,target);
        int[] expeted1 = new int[]{0,1};
        assertArrayEquals(actual1,expeted1);

        /* case two   [3,2,4] 6*/
        nums = new int[]{3,2,4};
        int[] actual2 = Solution1.twoSum(nums,target);
        int[] expeted2 = new int[]{1,2};
        assertArrayEquals(actual2,expeted2);

    }

}
