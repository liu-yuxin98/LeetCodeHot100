def quick_sort(nums):

    quick_sort_helper(0, len(nums)-1, nums)

    # def partition(left, right,array):
    #     pivot = array[right]
    #     while(left < right):
    #         while(left < right and array[left] <= pivot):
    #             left += 1
    #         array[right] = array[left]
    #         while (left < right and array[right] >= pivot):
    #             right -= 1
    #         array[left] = array[right]
    #     array[right] = pivot
    #     return right

    def partition(left, right, arr):
        target = arr[left]
        while left < right:
            while(left < right and arr[right] >= target):
                right -= 1
            arr[left] = arr[right]
            while(left < right and arr[left] <= target):
                left += 1
            arr[right] = arr[left]
        arr[left] = target
        return left

    def quick_sort_helper(start, end, nums):
        if start >= end:
            return
        index = partition(start, end, nums)
        quick_sort_helper(start, index-1, nums)
        quick_sort_helper(index+1, end, nums)
