# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 01:00:51 2021

@author: Lenovo
"""


# def findMedianSortedArrays(nums1, nums2):
#     """
#     :type nums1: List[int]
#     :type nums2: List[int]
#     :rtype: float
#     """
    
#     combined = []
#     if nums1 == []:
#         combined = nums2
#     elif nums2 == []:
#         combined = nums1
#     else:
#         p1 = 0
#         p2 = 0
#         while True:
#             if nums1[p1] >= nums2[p2]:
#                 combined.append(nums2[p2])
#                 p2 += 1
#                 if p2 >= len(nums2):
#                     combined += nums1[p1::]
#                     break
#             else:
#                 combined.append(nums1[p1])
#                 p1 += 1
#                 if p1 >= len(nums1):
#                     combined += nums2[p2::]
#                     break
#     n = len(combined)
#     if n % 2 == 0:
#         return float(combined[n//2-1] + combined[n//2])/2
#     else:
#         return combined[n//2]


# binary sort
def findMedianSortedArrays(nums1, nums2):
        def find_k_large(A,B,k):
            ''' find k'th largest number from A,B,         O(log(m+n))
            '''
            if A == []:
                return B[k-1]
            elif B == []:
                return A[k-1]
            else:      
                m = len(A)
                n = len(B)
                if k == 1:
                    return min(A[0],B[0])
                elif k == m+n:
                    return max(A[m-1],B[n-1])
                else:
                    i = (m+1)//2-1
                    j = (n+1)//2-1               
                    if k >= i+j+2:
                        if A[i] < B[j]:
                            return find_k_large(A[i+1::], B, k-(i+1))
                        elif A[i] > B[j]:
                            return find_k_large(A, B[j+1::], k-(j+1))
                        else:
                            if k==i+j+2:
                                return A[i]
                            return find_k_large(A[i+1::], B[j+1::],  k -(i+j+2))
                    else: # k<i+j+2
                        if A[i] < B[j]:
                            return find_k_large(A, B[0:j], k)
                        elif A[i] > B[j]:
                            return find_k_large(A[0:i], B, k)
                        else:                   
                            return find_k_large(A[0:i], B[0:j+1], k)
        m = len(nums1)
        n = len(nums2)
        if (m+n)%2 == 0:
            k = (m+n)//2
            value1 = find_k_large(nums1,nums2, k)
            value2 = find_k_large(nums1,nums2,k+1)
            return 1.0*(value1+value2)/2
        else:
            k = (m+n)//2 + 1
            value = find_k_large(nums1, nums2, k)
            return 1.0*value



def find_k_large(A,B,k):
    ''' find k'th largest number from A,B,         O(log(m+n))
    '''
    if A == []:
        return B[k-1]
    elif B == []:
        return A[k-1]
    else:      
        m = len(A)
        n = len(B)
        if k == 1:
            return min(A[0],B[0])
        elif k == m+n:
            return max(A[m-1],B[n-1])
        else:
            i = (m+1)//2-1
            j = (n+1)//2-1               
            if k >= i+j+2:
                if A[i] < B[j]:
                    return find_k_large(A[i+1::], B, k-(i+1))
                elif A[i] > B[j]:
                    return find_k_large(A, B[j+1::], k-(j+1))
                else:
                    if k==i+j+2:
                        return A[i]
                    return find_k_large(A[i+1::], B[j+1::],  k -(i+j+2))
            else: # k<i+j+2
                if A[i] < B[j]:
                    return find_k_large(A, B[0:j], k)
                elif A[i] > B[j]:
                    return find_k_large(A[0:i], B, k)
                else:                   
                    return find_k_large(A[0:i], B[0:j+1], k)


            
            
                
    
    
nums1 = [1,2]
nums2 = [3,4]
output = findMedianSortedArrays(nums1, nums2)
# A = [] 
# B = [0,1]
# k = 1
# k_large = find_k_large(A,B,k)