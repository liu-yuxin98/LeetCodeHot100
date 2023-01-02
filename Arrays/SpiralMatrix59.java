import java.lang.reflect.Array;
import java.util.Arrays;

public class SpiralMatrix59 {
    public int[][] generateMatrix(int n) {

        int [][] directions = new int[][]{{0,1},{1,0},{0,-1},{-1,0}};
        int direct = 0;
        int [][] res = new int[n][n];
        int row = 0;
        int col = 0;
        for(int i=1;i<=n*n;i++){
            System.out.println(row+" "+col+" "+i);
            boolean cond1 = row>=n || col >=n || row<0 || col<0 ;  // out of boundary
            boolean cond2 = row<n && row>=0 && col <n && col >=0 && res[row][col] != 0;  // already reached
            if(cond1 || cond2){
                // back one step
                row -= directions[direct % 4][0];
                col -= directions[direct % 4][1];
                // change direction
                direct ++;
                // move forward
                row += directions[direct % 4][0];
                col += directions[direct % 4][1];
            }
            res[row][col] = i;
            row += directions[direct % 4][0];
            col += directions[direct % 4][1];
        }
        return res;
    }
}
