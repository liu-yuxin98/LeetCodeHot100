public class QuickSort {
    public int[] quickSort(int[] arr, int left, int right) {
        if (left < right) {
            int partitionIndex = partition(arr, left, right);
            quickSort(arr, left, partitionIndex - 1);
            quickSort(arr, partitionIndex + 1, right);
        }
        return arr;
    }

    public int partition(int[] arr, int left, int right) {
        int pivot = arr[left]; //pivot value

        // scan from two sides to middle
        while(left<right){
            while (left<right && pivot <= arr[right]){
                right -= 1;
            }
            arr[left] = arr[right];

            while(left < right && pivot>=arr[left]){
                left += 1;
            }
            arr[right] = arr[left];
        }
        arr[left] = pivot;
        return left;
    }

}
