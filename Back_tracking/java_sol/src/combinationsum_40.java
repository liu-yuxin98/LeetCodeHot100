import java.util.*;

public class combinationsum_40 {
    List<List<Integer>> res = new ArrayList<>();
    LinkedList<Integer> path = new LinkedList<>();
    int sum = 0;

    public List<List<Integer>> combinationSum2( int[] candidates, int target ) {
        //为了将重复的数字都放到一起，所以先进行排序
        Arrays.sort( candidates );
        backTracking( candidates, target, 0 );
        return res;
    }

    private void backTracking( int[] candidates, int target, int start ) {
        if ( sum == target ) {
            res.add( new ArrayList<>( path ) );
            return;
        }
        for ( int i = start; i < candidates.length && sum + candidates[i] <= target; i++ ) {
            //正确剔除重复解的办法
            //跳过同一树层使用过的元素
            if ( i > start && candidates[i] == candidates[i - 1] ) {
                continue;
            }

            sum += candidates[i];
            path.add( candidates[i] );
            // i+1 代表当前组内元素只选取一次
            backTracking( candidates, target, i + 1 );

            int temp = path.getLast();
            sum -= temp;
            path.removeLast();
        }
    }
}
