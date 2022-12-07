import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class combinationSum_216 {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();
    public List<List<Integer>> combinationSum3(int k, int n) {
        backtrack(k,n,1);
        return res;
    }
    private void backtrack(int k, int n, int start){
        if(path.size()==k){
            if( path.stream().mapToInt(a->a).sum() ==n){
                res.add(new ArrayList<>(path));
            }
            return;
        }
        for(int i =start;i<=9;i++){
            path.add(i);
            start = Math.max(start+1,i+1);
            backtrack(k,n,start);
            path.remove(path.size() - 1);
        }
    }
}
