class Solution4(object):
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        totallength = len1+len2
        median = 0
        index = totallength/2 -1
        if totallength <=1:
            if len1:
                median = nums1[0]
            else:
                median = nums2[0]
        else:
            if totallength%2 == 0:



            else:




s = Solution4()
nums1 = []
nums2 = [1]
print(s.findMedianSortedArrays(nums1,nums2))