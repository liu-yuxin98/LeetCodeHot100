public class minSizeSubarray209 {
    public int minSubArrayLen(int target, int[] nums) {
        int front = 0;
        int end = 0;
        boolean found = false;
        int minlen = nums.length;
        int sum = 0;
        while(end<nums.length && front < nums.length){
            if(sum<target){
                sum+=nums[end];
                end++;
            }else{
                found = true;
                System.out.println(nums[front]+" "+nums[end]+" "+front+" "+end+" "+sum);
                minlen = Math.min(minlen,end-front);
                sum -= nums[front];
                front++;
            }
        }
        // end alreay reach end, end =n
        while(front< nums.length){
            if(sum>=target){
                found = true;
                sum -= nums[front];
                minlen = Math.min(minlen,end-front);
                front++;
            } else{
                break;
            }
        }

        if (found) {
            return minlen;
        }
        return 0;
    }
}
