package lintcode;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;

public class Easy607TwoSumDesign {
    /**
     * @param number: An integer
     * @return: nothing
     */
    private List<Integer> nums = new ArrayList<Integer>();
    private HashSet<Integer> sets = new HashSet<Integer>();
    public void add(int number) {
        // write your code here
        nums.add(number);

    }

    /**
     * @param value: An integer
     * @return: Find if there exists any pair of numbers which sum is equal to the value.
     */
    public boolean find(int value) {
        sets = new HashSet<Integer>();

        // write your code here
        for(Integer num:nums){
            if(sets.contains(value-num)){
                return true;
            }
            sets.add(num);
        }
        return false;
    }

    public static void main(String[] args) {
        Easy607TwoSumDesign easy607TwoSumDesign = new Easy607TwoSumDesign();
        easy607TwoSumDesign.add(2);
        easy607TwoSumDesign.add(3);
        System.out.println(easy607TwoSumDesign.find(4));
        easy607TwoSumDesign.add(3);
        System.out.println(easy607TwoSumDesign.find(6));
    }
}
