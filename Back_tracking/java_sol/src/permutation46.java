import java.util.*;
import java.util.stream.Collectors;

public class permutation46 {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();
    Boolean [] used;

    private void backtrack(int [] nums){
        if(path.size()==nums.length){
            res.add(new ArrayList<>(path));
            return;
        }

        for(int i = 0; i < nums.length; i++){
            if(used[i]){
                continue;
            }
            path.add(nums[i]);
            used[i] = true;
            backtrack(nums);
            path.remove(path.size() - 1);
            used[i] = false;
        }

    }

    public List<List<Integer>> permute(int[] nums) {
        used = new Boolean[nums.length];
        Arrays.fill(used,false);
        backtrack(nums);
        return res;
    }
}
