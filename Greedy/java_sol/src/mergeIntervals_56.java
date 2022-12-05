import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class mergeIntervals_56 {
    public static int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        List<List<Integer>> merged = new ArrayList<>();
        Integer start = intervals[0][0];
        Integer end = intervals[0][1];
        for(int i=0;i<intervals.length; i++){

            if(intervals[i][0] > end){
                // no overlap
                List<Integer> item = new ArrayList<>();
                item.add(start);
                item.add(end);
                merged.add(item);
                start = intervals[i][0];
                end = intervals[i][1];
            }else{
                // ovelap
                end = Math.max(end,intervals[i][1]);
            }
        }
        // the last one
        List<Integer> item = new ArrayList<>();
        item.add(start);
        item.add(end);
        merged.add(item);

        int [][] res = merged.stream().map(l->l.stream().mapToInt(Integer::intValue).toArray()).toArray(int[][]::new);

        return  res;
    }
    public static void main(String[] args) {
        int [][] intervals =        {
                {1,3},
                {2,6},
                {8,10},
                {15,18},
        };
        int[][] output = merge(intervals);
        System.out.println(Arrays.deepToString(output));
    }
}
