public class JumpGame_55 {
    public static boolean canJump(int[] nums) {
        int i = 0;
        int next_max = 0;
        int next_pos = 0;
        while(true){
            //find next pos
            next_max = i+nums[i];
            if(next_max>=nums.length-1){
                return true;
            }
            // can not move forward
            if(next_max==i){
                return false;
            } else{
                // find next_pos that can reach furthest
                for(int j=i+1;j<next_max+1;j++){
                    if(nums[j]+j>=nums[next_pos]+next_pos){
                        next_pos = j;
                    }
                }
            }
            i = next_pos;
        }

    }
    public static void main(String[] args) {
        int [] nums = new int[]{3,2,1,0,4};
        boolean output = canJump(nums);
        System.out.println(output);
    }
}
