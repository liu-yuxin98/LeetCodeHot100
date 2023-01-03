import java.util.*;

public class ThreeSum15 {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        Set<Set<Integer>> tempres = new HashSet<>();
        Arrays.sort(nums);
        int n = nums.length;
        // two pointer
        for (int i = 0; i < n-2; i++) {
            if (nums[i] >0 ) {
                return res;
            }
            if(i>0 && nums[i]==nums[i-1]){
                continue;
            }
            int left = i+1;
            int right = n-1;

            while(right>left){
                int sum = nums[i]+nums[left]+nums[right];
                if(sum==0){
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    // remove duplicate, b  c
                    while (right > left && nums[right] == nums[right - 1]) right--;
                    while (right > left && nums[left] == nums[left + 1]) left++;
                    right--;
                    left++;
                } else if(sum>0){
                    right --;
                }else{
                    left ++;
                }

            }
        }
        return res;

    }


}
