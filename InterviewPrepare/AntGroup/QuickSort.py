def quickSort(nums):
    quickSort(nums, 0, len(nums)-1)


def quickSortHelper(nums, start, end):
    index = partition(nums, start, end)
    quickSort(nums, start, index-1)
    quickSort(nums, index+1, end)


def partition(nums, start, end):
    pivot = nums[end]
    i = start-1
    for j in range(start, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    return index
