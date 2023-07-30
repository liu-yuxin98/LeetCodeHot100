import Interview150.Solution88MergeSortedArray;
import org.junit.Assert;
import org.junit.Test;

public class Executor {
    @Test
    public void test88() {
        Solution88MergeSortedArray solution88MergeSortedArray = new Solution88MergeSortedArray();
        int[] nums1 = new int[]{1, 2, 3, 0, 0, 0};
        int m = 3;
        int[] nums2 = new int[]{2, 5, 6};
        int n = 3;
        solution88MergeSortedArray.merge(nums1,m,nums2,n);
        int [] expected = new int[]{1,2,2,3,5,6};
        Assert.assertArrayEquals(nums1,expected);

    }

}
