
# Python3 implementation of QuickSort
def quickSort(nums):
    quick_sort(nums, 0, len(nums)-1)

# Function to find the partition position


def partition(array, low, high):
    pivot = array[low]
    while(low < high):
        while(low < high and array[high] >= pivot):
            high -= 1
        # find a array[right] < pivot
        array[low] = array[high]
        while(low < high and array[low] <= pivot):
            low += 1
        array[high] = array[low]
    array[low] = pivot
    return low

# Function to perform quicksort


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quick_sort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort(array, pi + 1, high)


# Driver code
array = [10, 7, 8, 9, 1, 5]

quickSort(array)

print(f'Sorted array: {array}')
