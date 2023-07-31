package hot150;

import java.util.Arrays;

public class Easy88MergeSortedArray {
    public static void merge(int[] nums1, int m, int[] nums2, int n) {
        if(m==0){
            System.arraycopy(nums2, 0, nums1, 0, n);
        }else if(n>0){
            // move num in nums1 back to the end
            for(int i=nums1.length - 1;i>=n;i--){
                nums1[i] = nums1[i-n];
            }
            int p1 = n;
            int p2 = 0;
            int p = 0;
            while (true) {
                if(nums1[p1]<=nums2[p2]){
                    nums1[p] = nums1[p1];
                    p1++;
                    p++;
                    if(p1==m+n){
                        while (p2<n){
                            nums1[p] = nums2[p2];
                            p++;
                            p2++;
                        }
                        break;
                    }
                }else{
                    nums1[p] = nums2[p2];
                    p2++;
                    p++;
                    if(p2==n){
                        break;
                    }
                }


            }

        }

    }


    public static void main(String[] args) {
        int[] nums1 = {1,2,4,5,6,0};
        int m =5;
        int [] nums2 = {3};
        int n = 1;
        merge(nums1,m,nums2,n);
        System.out.println(Arrays.toString(nums1));
    }
}
