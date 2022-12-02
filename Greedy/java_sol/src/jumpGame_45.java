public class jumpGame_45 {
    public static int jump(int[] nums) {
        if(nums.length<=1){
            return 0;
        }
        int i = 0;
        int next_max = 0;
        int next_pos = 0;
        int step = 1;
        while(true){
            //find next pos
            next_max = i+nums[i];
            if(next_max>=nums.length-1){
                return step;
            }
            // can not move forward
            if(next_max==i){
                return -1;
            } else{
                // find next_pos that can reach furthest
                for(int j=i+1;j<next_max+1;j++){
                    if(nums[j]+j>=nums[next_pos]+next_pos){
                        next_pos = j;
                    }
                }
            }
            i = next_pos;
            step += 1;
        }

    }

    public static void main(String[] args) {
        int [] nums = new int[]{2,3,0,1,4};
        int output = jump(nums);
        System.out.println(output);
    }
}
