package leetcodeContest.Contest356;

public class NumEmployeeMetTarget {
    public static int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int cnt = 0;
        for(int hour:hours){
            if(hour>=target){
                cnt+=1;
            }
        }
        return cnt;
    }

    public static void main(String[] args) {
        int [] hours  = new int[] {
            0,1,2,3,4
        };
        int target = 2;
        int out = numberOfEmployeesWhoMetTarget(hours,target);
        System.out.println(out);
    }
}
