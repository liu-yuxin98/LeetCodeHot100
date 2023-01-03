import java.util.*;

public class FourSum18 {

    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> res = kSum(nums,target,4);
        return res;
    }

    public List<List<Integer>> kSum(int[] nums, int target, int k){

        if(k> nums.length){
            return new ArrayList<>();
        }

        // check if target can be satisfied
        long max = 0;
        long min = 0;
        for(int i = 0; i < k; i++){
            min += nums[i];
        }
        for(int i=nums.length - 1; i >= nums.length-k; i--){
            max += nums[i];
        }
        if(target < min || target > max){
            return new ArrayList<>();
        }

        if(k==2){
            return twoSum(nums, target, 0);
        }


        List<List<Integer>> res = new ArrayList<>();
        for(int i = 0; i < nums.length; i++){
            if(i>0){
                if(nums[i] == nums[i-1]){
                    continue;
                }
            }
            int [] subnums = Arrays.copyOfRange(nums,i+1,nums.length);
            List<List<Integer>> nextLayerRes = kSum( subnums,target-nums[i],k-1 );
            if(nextLayerRes==null){
                continue;
            }
            for(List<Integer> combination: nextLayerRes){
                combination.add(nums[i]);
                res.add(new ArrayList<>(combination));
            }
        }
        return res;
    }

    public List<List<Integer>> twoSum(int[]nums, int target, int start){
            int low = start;
            int high = nums.length-1;
            List<List<Integer>> res = new ArrayList<>();
            while(low<high){
                int sum = nums[low]+nums[high];
                if(sum>target){
                    high --;
                } else if(sum<target){
                    low++;
                } else{
                    //sum==target
                    List<Integer> twoIndexes = new ArrayList<>();
                    twoIndexes.add(nums[low]);
                    twoIndexes.add(nums[high]);
                    res.add(new ArrayList<>(twoIndexes));
                    // skip duplicate
                    while(low<high && nums[low]==nums[low+1]){
                        low++;
                    }
                    while(low<high && nums[high]==nums[high-1]){
                        high--;
                    }
                    low++;
                    high--;
                }
            }
            return res;
    }
//    public List<List<Integer>> fourSum(int[] nums, int target) {
//        Arrays.sort(nums);
//        HashMap<Integer, List<int[]>> map = new HashMap< Integer, List<int[] >>();
//        for(int i=0;i<nums.length-1; i++){
//            for(int j=i+1;j<nums.length; j++){
//                if(map.containsKey(nums[i]+nums[j])){
//                    map.get(nums[i]+nums[j]).add(new int[]{i,j});
//                }else{
//                    List<int[]> temp = new ArrayList<int[]>();
//                    temp.add(new int[]{i,j});
//                    map.put(nums[i]+nums[j], new ArrayList<>(temp));
//                }
//            }
//        }
//
//        List<Set<Integer>> tempres = new ArrayList<>();
//
//        for(Integer firstSum: map.keySet()){
//            if(firstSum>target){
//                break;
//            }
//            if(map.containsKey(target-firstSum)){
//                List<int []> firstCombinations = map.get(firstSum);
//                List<int []> secondCombinations = map.get(target-firstSum);
//                for(int [] firstCombined:firstCombinations){
//                    for(int [] secondCombined:secondCombinations){
//                        if(firstCombined[0] == secondCombined[0] || firstCombined[0] ==secondCombined[1]
//                        || firstCombined[1]==secondCombined[0] || firstCombined[1]==secondCombined[1]){
//                            // duplicate use same item
//                            continue;
//                        }
//                        // no duplication
//                        Set<Integer> temp = new HashSet<>();
//                        temp.add(nums[firstCombined[0]]);
//                        temp.add(nums[firstCombined[1]]);
//                        temp.add(nums[secondCombined[0]]);
//                        temp.add(nums[secondCombined[1]]);
//                        if(!tempres.contains(temp)){
//                            tempres.add(new HashSet<>(temp));
//                        }
//                    }
//
//                }
//
//
//            }
//
//        }
//
//        System.out.println(tempres);
//        return null;
//    }
}
