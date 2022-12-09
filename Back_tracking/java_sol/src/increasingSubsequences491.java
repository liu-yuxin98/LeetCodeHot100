import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class increasingSubsequences491 {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();
    HashSet<List<Integer>> resSet;
    private void backtrack(int [] nums, int start){
        if(path.size() >= 2){
            resSet.add(new ArrayList<>(path));
        }
        if(start>=nums.length){
            return;
        }

        for(int i=start;i< nums.length;i++){
            if(i > 0){
                if(path.size()>0 && nums[i] < path.get(path.size() - 1)){
                    continue;
                }
            }
            path.add(nums[i]);
            backtrack(nums,i+1);
            path.remove(path.size() - 1);
        }

    }
    public List<List<Integer>> findSubsequences(int[] nums) {
        resSet = new HashSet<>();
        backtrack(nums,0);
        res = new ArrayList<>(resSet);
        return res;
    }
}
