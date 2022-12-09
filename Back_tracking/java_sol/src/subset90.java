import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class subset90 {

    List<List<Integer>> res = new ArrayList<>();
    HashSet<List<Integer>> hset = new HashSet<>();
    List<Integer> path = new ArrayList<>();
    boolean[] used;
    private void backtrak(int[] nums, int start){
        res.add(new ArrayList<>(path));
        if(start>=nums.length){
            return;
        }

        for(int i=start;i < nums.length; i++){
            if(i>=1 && nums[i] == nums[i-1] && !used[i-1]){
                continue;
            }
            path.add(nums[i]);
            used[i] = true;
            backtrak(nums,i+1);
            path.remove(path.size() - 1);
            used[i] = false;
        }
    }
    public List<List<Integer>> subsetsWithDup(int[] nums) {
            if(nums.length == 0){
                res.add(path);
                return res;

            }
            Arrays.sort(nums);
            used = new boolean[nums.length];
            backtrak(nums,0);
            return res;
    }
}
