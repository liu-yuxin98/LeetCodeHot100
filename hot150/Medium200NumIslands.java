package hot150;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.Stack;

public class Medium200NumIslands {

    private static int[][] generateDirections() {
        int[][] directions = new int[4][2];
        // up
        directions[0][0] = -1;
        directions[0][1] = 0;
        //down
        directions[1][0] = 1;
        directions[1][1] = 0;
        // left
        directions[2][0] = 0;
        directions[2][1] = -1;
        //right
        directions[3][0] = 0;
        directions[3][1] = 1;
        return directions;
    }

    public static char[][] generateNewGrid(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        // update grid
        char[][] newGrid = new char[m + 2][n + 2];
        for (int i = 0; i < m + 2; i++) {
            newGrid[i][0] = '0';
            newGrid[i][n + 1] = '0';
        }
        for (int j = 0; j < n + 2; j++) {
            newGrid[0][j] = '0';
            newGrid[m + 1][j] = '0';
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                newGrid[i + 1][j + 1] = grid[i][j];
            }
        }
        return newGrid;
    }


    public static void dfs(char[][] newGrid, Stack<int[]> queue) {
        while (queue.size() > 0) {
            int[] item = queue.pop();
            int x = item[0];
            int y = item[1];
            int[][] directions = generateDirections();
            for (int[] direction : directions) {
                if (newGrid[x + direction[0]][y + direction[1]] == '1') {
                    newGrid[x + direction[0]][y + direction[1]] = 'Y';
                    queue.add(new int[]{x + direction[0], y + direction[1]});
                    dfs(newGrid, queue);
                }
            }
        }

    }

    //dfs
    public static int numIslandsDFS(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int cnt = 0;
        // update grid
        char[][] newGrid = generateNewGrid(grid);
        // dfs FILO
        Stack<int[]> queue = new Stack<int[]>();
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (newGrid[i][j] == '1') {
                    cnt++;
                    newGrid[i][j] = 'Y';
                    queue.add(new int[]{i, j});
                    dfs(newGrid, queue);
                }
            }
        }
        System.out.println(Arrays.deepToString(newGrid));
        return cnt;
    }

    // bfs
    public static int numIslandsBFS(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        // update grid
        char[][] newGrid = generateNewGrid(grid);
        int[][] directions = generateDirections();

        int cnt = 0;
        for (int i = 1; i < m + 1; i++) {
            for (int j = 1; j < n + 1; j++) {
                if (newGrid[i][j] == '1') {
                    cnt++;
                    // bfs to change this island to 'Y'
                    //FIFO queue
                    Deque<int[]> queue = new ArrayDeque<>();
                    queue.add(new int[]{i, j});
                    while (queue.size() > 0) {
                        int[] item = queue.removeFirst();
                        int x = item[0];
                        int y = item[1];
                        newGrid[x][y] = 'Y';
                        // find neighbors
                        for (int[] direction : directions) {
                            if (newGrid[x + direction[0]][y + direction[1]] == '1') {
                                newGrid[x + direction[0]][y + direction[1]] = 'Y';
                                queue.add(new int[]{x + direction[0], y + direction[1]});
                            }
                        }
                    }
                }
            }
        }

        return cnt;
    }


    public static void main(String[] args) {
//        char[][] grid = {
//                        {'1','1','1','1','0'},
//                        {'1','1','0','1','0'},
//                        {'1','1','0','0','0'},
//                        {'0','0','0','0','0'},
//                        };

//        char [][] grid = {
//                {'1','1','1'},
//                {'0','1','0'},
//                {'1','1','1'}
//        };
        char[][] grid = {
                {'1', '1', '0', '0', '0'},
                {'1', '1', '0', '0', '0'},
                {'0', '0', '1', '0', '0'},
                {'0', '0', '0', '1', '1'},
        };

        System.out.println(numIslandsDFS(grid));

    }
}
