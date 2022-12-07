
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;
class combination_77 {
    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new LinkedList<>();
    public List<List<Integer>> combine(int n, int k) {
        combineHelper(n,k,1);
        return res;
    }
    private void combineHelper(int n, int k, int start){
        if(path.size()==k){
            res.add(new ArrayList<>(path));
            return;
        }
        for(int i = start; i <=n; i++){
            path.add(i);
            start = Math.max(i+1,start+1);
            combineHelper(n,k,start);
            path.remove(path.size() - 1);
        }
    }


}

