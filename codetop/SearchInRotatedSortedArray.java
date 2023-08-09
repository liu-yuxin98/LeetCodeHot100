package codetop;

public class SearchInRotatedSortedArray {

    public int search(int[] nums, int target) {

        //rotated
        if (nums[0] > nums[nums.length - 1]) {
            int rotationIndex = findRotationIndex(nums);
            if(target>=nums[0]){
                //find between [0,rotationIndex]
                return binarySearch(nums,0,rotationIndex,target);
            }else{
                return binarySearch(nums,rotationIndex,nums.length - 1,target);
            }
        }
        // not rotated
        // binary search through the nums to find if target exist
        return binarySearch(nums,0,nums.length-1,target);
    }

    public int findRotationIndex(int [] nums){

        int left = 0;
        int right = nums.length-1;
        int mid = (left+right)/2;
        // find rotation point
        while(true){
            if(mid==0){
                return 1;
            }
            if(mid==nums.length - 1){
                return nums.length-1;
            }
            if(nums[mid]<nums[mid-1] && nums[mid]<nums[mid+1]){
                return mid;
            }
            else if(nums[mid]>nums[0]){
                left =mid+1;
            }  else{
                right = mid-1;
            }
            mid = (left+right)/2;
        }
    }
    public int binarySearch(int[] nums, int left, int right, int target){
        int mid = (left + right) / 2;
        while (left <= right) {
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
            mid = (left+right)/2;
        }
        return -1;
    }

    public static void main(String[] args) {
        SearchInRotatedSortedArray solution = new SearchInRotatedSortedArray();
        int [] nums = {5,1,2,3,4};
        int target = 1;
        System.out.println(solution.search(nums,target));
    }

}
