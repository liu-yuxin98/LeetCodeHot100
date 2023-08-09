package codetop;

import java.util.PriorityQueue;

public class KthLargestElementInArray {

    public static int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>();
        for (int i = 0; i < k; i++) {
            maxHeap.add(nums[i]);
        }
        for (int i = k; i < nums.length; i++) {
            if (nums[i] > maxHeap.peek()) {
                maxHeap.poll();
                maxHeap.add(nums[i]);
            }
        }
        return maxHeap.peek();
    }

    public static void main(String[] args) {
        int[] nums = {3, 2, 1, 5, 6, 4};
        System.out.println(findKthLargest(nums, 2));
    }
}
