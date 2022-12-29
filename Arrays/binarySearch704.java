public class binarySearch704 {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        int mid;
        while (left <= right) {
            mid = (left+right)/2;
            if(nums[mid]==target){
                return mid;
            } else if(nums[mid]>target){
                right = mid -1;
            } else{
                left = mid + 1;
            }
        }
        return -1;
    }
//        int left =0;
//        int right = nums.length-1;
//        int mid = (left+right)/2;
//
//        while(true){
//            if(nums[mid]==target){
//                return mid;
//            }
//            if(nums[mid] > target){
//                right = mid;
//            }
//            else if(nums[mid]<target){
//                left = mid;
//            }
//            mid = (left+right)/2;
//            if(mid==left){
//                if(nums[mid]==target){
//                    return mid;
//                } else if(mid+1 <nums.length && nums[mid+1]==target){
//                    return mid+1;
//                }
//                return -1;
//            }
//        }
//
//    }
//
}
