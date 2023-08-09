package codetop;

import java.util.*;

public class ThreeSum {
    public static List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> resSet = new HashSet<>();
        List<List<Integer>> res = new ArrayList<>();
        HashMap<Integer,Integer> map ;
        for (int i = 0; i < nums.length-2; i++) {
            int target = -nums[i];
            if(target<0){
                break;
            }
            map = new HashMap<>();
            for (int j = i+1; j <nums.length; j++) {
                if(map.containsKey(target-nums[j])){
                    resSet.add(List.of(nums[i],nums[map.get(target - nums[j])],nums[j]));
                }else{
                 map.put(nums[j],j);
                }
            }
        }
        for(List<Integer> item:resSet){
            res.add(item);
        }
        return res;
    }

    public static List<List<Integer>> threeSumTwoPointer(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> resSet = new HashSet<>();
        List<List<Integer>> res = new ArrayList<>();
        HashMap<Integer,Integer> map ;
        for (int i = 0; i < nums.length-2; i++) {
            int target = -nums[i];
            if(target<0){
                break;
            }
            int small = i+1;
            int large = nums.length-1;
            while(small<large){
                if(nums[small]+nums[large]==target){
                    resSet.add(List.of(nums[i],nums[small],nums[large]));
                    small++;
                    large--;
                }else if(nums[small]+nums[large] > target){
                    large--;
                }   else{
                    small++;
                }
            }

        }
        res.addAll(resSet);
        return res;
    }

    public static void main(String[] args) {
        int[] nums = {0,0,0,0};
        System.out.println(threeSum(nums));
    }

}
