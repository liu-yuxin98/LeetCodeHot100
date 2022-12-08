import java.util.ArrayList;
import java.util.List;

public class subset78 {

    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();

    private void backtrack(int[] nums, int start, int layer){
        if(layer>nums.length){
            return;
        }
        for(int i=start;i<nums.length;i++){
            path.add(nums[i]);
            res.add(new ArrayList<>(path));
            backtrack(nums,i+1, layer+1);
            path.remove(path.size() - 1);
        }

    }
    public List<List<Integer>> subsets(int[] nums) {
        res.add(path);
        backtrack(nums,0,0);
        return res;
    }
}
