package hot150;

public class Medium209MinimumSizeSubArraySum {
    public static int minSubArrayLen(int target, int[] nums) {
        int front = 0;
        int end = 0;
        int curMin = nums.length + 1;
        int curSum = nums[0];
        while (true) {
            // already min
            if (curMin == 1) {
                return 1;
            }

            while (curSum >= target) {
                curMin = Math.min(curMin, end - front + 1);
                curSum -= nums[front];
                front++;
            }
            end++;
            if(end>=nums.length){
                break;
            }
            curSum += nums[end];
        }
        // not find
        if (curMin > nums.length) {
            return 0;
        }
        return curMin;
    }

    public static void main(String[] args) {
        int target = 4;
        int[] nums = {1,4,4,3};
        System.out.println(minSubArrayLen(target,nums));
    }

}
