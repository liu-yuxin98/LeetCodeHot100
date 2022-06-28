import org.junit.Test;

import java.util.ArrayList;
import java.util.List;

import static org.junit.Assert.*;

/*Given two sorted arrays nums1 and nums2 of size m and n respectively,
return the median of the two sorted arrays.
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。*/
/*The overall run time complexity should be O(log (m+n)).*/
public class Solution4 {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        List<Integer> nums = new ArrayList<>();
        int i = 0;
        int j = 0;
        while(i<nums1.length && j<nums2.length){
            if(nums1[i]<=nums2[j]){
                nums.add(nums1[i]);
                i += 1;
            } else{
                nums.add(nums2[j]);
                j+= 1;
            }
        }
        if(i == nums1.length){
            while(j<nums2.length){
                nums.add(nums2[j]);
                j+= 1;
            }

        } else{
            /* j == nums2.length*/
            while(i<nums1.length){
                nums.add(nums1[i]);
                i+= 1;
            }
        }

        boolean isEven = (nums.size()%2 == 0);
        int midindex = nums.size() / 2;
        double res = 0;
        if(nums.size()<2){
            res = 1.0 * nums.get(0);
        }

        if(isEven){
            midindex -= 1;
            res = (1.0*nums.get(midindex)+nums.get(midindex+1))/2;
        } else{
            res = 1.0*nums.get(midindex);
        }
        return res;

    }



    @Test
    public void Testcases(){
        int[] nums1 = new int[]{1,3};
        int[] nums2 = new int[]{2};
        double expected = 2;
        double actual = findMedianSortedArrays(nums1,nums2);
        assertEquals(expected,actual,0.0001);

        nums1 = new int[]{1,2};
        nums2 = new int[]{3,4};
        expected = 2.5;
        actual = findMedianSortedArrays(nums1,nums2);
        assertEquals(expected,actual,0.0001);


        nums1 = new int[]{0};
        nums2 = new int[]{0};
        expected = 0;
        actual = findMedianSortedArrays(nums1,nums2);
        assertEquals(expected,actual,0.0001);

        nums1 = new int[]{};
        nums2 = new int[]{1};
        expected = 1;
        actual = findMedianSortedArrays(nums1,nums2);
        assertEquals(expected,actual,0.0001);

        nums1 = new int[]{2};
        nums2 = new int[]{};
        expected = 2;
        actual = findMedianSortedArrays(nums1,nums2);
        assertEquals(expected,actual,0.0001);
    }
}


