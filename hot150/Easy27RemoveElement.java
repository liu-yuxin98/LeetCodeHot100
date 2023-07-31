package hot150;

import java.util.Arrays;

public class Easy27RemoveElement {
    public static int removeElement(int[] nums, int val) {
        int cnt = 0;
        for (int i = 0; i < nums.length; i++) {
            if(nums[i] == val){
                cnt++;
            }else{
                nums[i-cnt] = nums[i];
            }
        }

        return nums.length-cnt;

    }


    public static void main(String[] args) {
            int[] nums = {
                    3,2,2,3
            };
            int val =3;
            int k = removeElement(nums,val);
            System.out.println(k);
            System.out.println(Arrays.toString(nums));
    }

}
