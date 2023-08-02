package hot150;

import java.util.HashSet;
import java.util.Set;

public class Medium36ValidSudoku {
    public static boolean isValidSudoku(char[][] board) {

        // verify rows
        for(char[] row:board){
            Set<Character> rowNums = new HashSet<Character>();
            for(char num:row){
                if(Character.isDigit(num)) {
                    if (rowNums.contains(num)) {
                        return false;
                    } else {
                        rowNums.add(num);
                    }
                }
            }
        }
        // verify columns
        for(int j=0;j<9;j++){
            Set<Character> colNums = new HashSet<Character>();
            for(int i=0;i<9;i++){
                if(Character.isDigit(board[i][j])){
                    if(colNums.contains(board[i][j])){
                        return false;
                    }else{
                        colNums.add(board[i][j]);
                    }
                }
            }
        }
        // verify small grid
        for(int i=0;i < 9; i+=3){
            for(int j = 0; j < 9; j+=3){
                Set<Character> gridnums = new HashSet<Character>();
                for(int x=i;x<i+3;x++){
                    for (int y = j; y < j+3; y++) {
                        if(Character.isDigit(board[x][y])){
                            if(gridnums.contains(board[x][y])){
                                return false;
                            }else{
                                gridnums.add(board[x][y]);
                            }
                        }
                    }
                }

            }

        }
        return true;
    }

    public static void main(String[] args) {

    }
}
