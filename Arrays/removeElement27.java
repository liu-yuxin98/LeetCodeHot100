public class removeElement27 {
    public int removeElement(int[] nums, int val) {
        int cnt = 0;
        for(int i = 0; i < nums.length; i++){
            if(nums[i] == val){
                cnt += 1;
                continue;
            }
            // move forward cnt position
            nums[i-cnt] = nums[i];

        }
        return nums.length-cnt;

    }
}
