def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    m = len(nums1)
    n = len(nums2)
    # special cases
    if m == 0:
        if n % 2 == 0:
            return (nums2[n//2]+nums2[n//2-1])/2
        else:
            return nums2[n//2]
    if n == 0:
        if m % 2 == 0:
            return (nums1[m//2]+nums1[m//2-1])/2
        else:
            return nums1[m//2]
    # general cases
    i = 0
    j = 0
    cnt = 0  # count how many numbers have been add to vertual list
    nums1end = False
    nums2end = False
    if (m+n) % 2 == 0:
        # (m+n)//2 (m+n)//2 + 1 shoud be calculated
        while i < m and j < n:

            if nums1[i] >= nums2[j]:
                j += 1
                cnt += 1
                if cnt == (m+n)//2:
                    first = nums2[j-1]
                    if j >= n:
                        nums2end = True
                        second = nums1[i]
                    else:
                        if nums1[i] >= nums2[j]:
                            second = nums2[j]
                        else:
                            second = nums1[i]

                    return (first+second)/2
                if j >= n:
                    nums2end = True
                    # we need to find num in nums1
                    while i < m:
                        cnt += 1
                        if cnt == (m+n)//2:
                            first = nums1[i]
                            second = nums1[i+1]
                            return (first+second)/2
                        i += 1
            else:
                i += 1
                cnt += 1
                if cnt == (m+n)//2:
                    first = nums1[i-1]
                    if i >= m:  # nums1 reach end
                        nums1end = True
                        second = nums2[j]
                    else:
                        if nums1[i] >= nums2[j]:
                            second = nums2[j]
                        else:
                            second = nums1[i]
                    return (first+second)/2
                if i >= m:
                    nums1end = True
                    # we need to find num in nums2
                    while j < n:
                        cnt += 1
                        if cnt == (m+n)//2:
                            first = nums2[j]
                            second = nums2[j+1]
                            return (first+second)/2
                        j += 1
    else:
        # (m+n)//2+1 shoud be calculated
        while i < m and j < n:
            if nums1[i] >= nums2[j]:
                j += 1
                cnt += 1
                if cnt == (m+n)//2 + 1:
                    return nums2[j-1]
                elif j >= n:
                    nums2end = True
                    while i < m:
                        cnt += 1
                        if cnt == (m+n)//2+1:
                            return nums1[i]
                        i += 1
            else:
                i += 1
                cnt += 1
                if cnt == (m+n)//2 + 1:
                    return nums1[i-1]
                elif i >= m:
                    nums1end = True
                    while j < n:
                        cnt += 1
                        if cnt == (m+n)//2+1:
                            return nums2[j]
                        j += 1
