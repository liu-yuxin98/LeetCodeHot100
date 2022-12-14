import java.util.AbstractList;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class nQueens51 {


    List<List<Integer>> res = new ArrayList<>();
    List<Integer> path = new ArrayList<>();

    private boolean isvaild(List<Integer> path, Integer n){
        // only check the last to see if the last is inconsistent with previous
        for(int i=0;i<path.size()-1;i++){
            if(Objects.equals(path.get(path.size() - 1), path.get(i)) ||
                    path.get(path.size() - 1) == path.get(i)+(path.size() - 1-i) ||
                        path.get(path.size() - 1) == path.get(i)-(path.size() - 1-i) ){
                return false;
            }

        }
        return true;
    }

    private List<String> convert(List<Integer> path){
        List<String> sol = new ArrayList<>();
        for(int i = 0; i < path.size(); i++){
            StringBuilder sb = new StringBuilder();
            for(int j = 0; j < path.size(); j++){
                if(j==path.get(i)){
                    sb.append('Q');
                }else{
                    sb.append('.');
                }
            }
            String row = sb.toString();
            sol.add(row);
        }
        return sol;
    }

    private void backtrack(Integer col,Integer n){

        if(col>=n){
            res.add(new ArrayList<>(path));
            return;
        }

        for(int i=0;i<n;i++){

            path.add(i);
            // check if current path is vaild
            if (!isvaild(path, n)){
                path.remove(path.size()-1);
                continue;
            }
            backtrack(col+1,n);
            path.remove(path.size()-1);
        }

    }

    public List<List<String>> solveNQueens(int n) {
        backtrack(0,n);
        System.out.println(res.size());
        List<List<String>> allSolution = new ArrayList<>();
        for(int i = 0; i < res.size(); i++){
            List<String> solution = convert(res.get(i));
            allSolution.add(solution);
        }
        return allSolution;
    }
}
