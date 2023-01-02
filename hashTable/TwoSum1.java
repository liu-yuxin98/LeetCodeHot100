import java.util.HashMap;

public class TwoSum1 {

    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if(map.containsKey(nums[i])){
                int [] res = new int[]{ map.get(nums[i]),i};
                return res;
            }
            map.put(target-nums[i],i);
        }
        return null;
    }
}
