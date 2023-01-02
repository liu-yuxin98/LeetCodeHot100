import java.util.Arrays;
import java.util.HashMap;

public class FourSum454 {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        int n = nums1.length;
        int cnt = 0;
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                map.put( - (nums1[i] + nums2[j]), map.getOrDefault(-(nums1[i] + nums2[j]), 0) + 1);
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cnt += map.getOrDefault(nums3[i]+nums4[j],0);
            }
        }
        return cnt;
    }
}
