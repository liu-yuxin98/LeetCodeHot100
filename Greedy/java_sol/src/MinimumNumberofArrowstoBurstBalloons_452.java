import java.util.Arrays;
import java.util.Comparator;

public class MinimumNumberofArrowstoBurstBalloons_452 {
    public static int findMinArrowShots(int[][] points) {
        int cnt = 1;
        Arrays.sort(points, (a, b) -> Integer.compare(a[0], b[0]));
        System.out.println(Arrays.deepToString(points));
        for(int i=1;i<points.length; i++){
            if(points[i][0] >points[i-1][1]){
                cnt ++;
            } else{
                points[i][1] = Math.min(points[i][1],points[i-1][1]);
            }
        }

    return cnt;
    }
    public static void main(String[] args) {
        int [][] points =        {
                {3,9},
                {7,12},
                {3,8},
                {6,8},
                {9,10},
                {2,9},
                {0, 9},
                {3,9},
                {0, 6},
                {2,8},

        };
        int output = findMinArrowShots(points);
        System.out.println(output);
    }
}
