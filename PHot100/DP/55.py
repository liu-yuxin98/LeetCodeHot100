# -*- coding: utf-8 -*-
"""
Created on Sat May  8 09:30:44 2021

@author: Liu yuxin
"""
def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    
    
    
    
    # dp here is too slow
    # # initialization
    # n = len(nums)
    # f = [False]*n
    # f[0] = True
    # # DP process
    # for j in range(1, n):
    #     # previous stone is i
    #     # check if it can jump from i to j: two conditions should be satisfied
    #     # (1) can jump to f[i]
    #     # (2) i+nums[i] >= j
    #     for i in range(j):
    #         if f[i] and i+nums[i] >= j:
    #             f[j] = True
    #             if j+nums[j] >= n-1:
    #                 f[n-1] = True
    #             break
    #     if f[n-1] is True:
    #         break
    # return f[n-1]


def greedyJump(nums):
    if len(nums) <= 1:
        return True
    curmaxdis = nums[0]  # max position can be reached from current position
    nextmaxdis = 0  # max position can be reached for next jump
    currentp = 0  # current position
    nextp = curmaxdis  # next position
    while currentp < len(nums):
        # search nextp
        # from currentp to curmaxdis, find the nextp to get
        # max nextp+nums[nextp]
        curmaxdis = currentp + nums[currentp]
        for p in range(currentp, curmaxdis):
            if curmaxdis <= p + nums[p]:
                if p + nums[p] > nextmaxdis:
                    nextmaxdis = p + nums[p]
                    nextp = p
                    if nextmaxdis >= len(nums)-1:
                        return True
        # can't move forward
        if nextp == currentp:
            return False
        currentp = nextp
        curmaxdis = nextmaxdis
    # if go through all the iteration still can reach last item-> return false
    return False
        

            

                



nums = [0]
print(canJump(nums))
print(greedyJump(nums))