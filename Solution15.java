import org.junit.Test;

import java.util.*;
import java.util.stream.Collectors;

import static org.junit.Assert.*;

public class Solution15 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        List<Integer> item = new ArrayList<>();
        res.add(item);
        /* nums.length <4 */
        if(nums.length<4){
            /* nums.length = 3*/
            if(nums.length == 3){
                if(nums[0]+ nums[1]+nums[2] == 0){
                    int [] pos = new int[]{1,2,3};
                    List<Integer> itemi = Arrays.stream(pos).boxed().collect(Collectors.toList());
                    res.add(itemi);
                }
            }
            return res;
        }

        /*       length>=4             */

        /* rank the nums*/
        Arrays.sort(nums);
        /* min>0 and max<0 reurn []*/
        if(nums[0]>0 || nums[nums.length-1]<0){
            return res;
        }

        /* nums.length>4 and min<=0 max>=0*/
        



        return null;
    }
    @Test
    public void TestSolution15(){
        int [] nums = new int[]{-1,0,1,2,-1,-4};
        List<List<Integer>> autual = threeSum(nums);

        nums = new int[]{};
        autual = threeSum(nums);

        nums = new int[]{0};
        autual = threeSum(nums);



    }

}
