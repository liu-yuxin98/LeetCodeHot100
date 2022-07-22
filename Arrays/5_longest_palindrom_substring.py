# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 22:34:03 2022

@author: yuxin_liu_1998
"""

def longestPalindrome(s: str) -> str:
        
        # special cases len(s)<=2
        if len(s) <= 1:
            return s
        elif len(s) == 2:
            if s[0] == s[-1]:
                return s
            return s[0]
        
        max_s = s[0]
        # len(s) >=3
        mid = 1
        while True:
            if mid >= len(s)-1:
                break
            mid_l = mid -1
            mid_r = mid +1
            # find (mid_l,mid_r) are all s[mid]
            while mid_l >= 0:
                if s[mid_l] != s[mid]:
                    break
                mid_l -= 1
    
            while mid_r < len(s):
                if s[mid_r] != s[mid]:
                    break
                mid_r += 1
            
            # using (mid_l, mid_r) as center
            left = mid_l
            right = mid_r
            while True:
                if left < 0:
                    if right-left-1 > len(max_s):
                        max_s = s[left+1:right]
                    break
                elif right >= len(s):
                    if right-left-1 > len(max_s):
                        max_s = s[left+1:right]
                    break                
                if s[left] != s[right]:
                    if right-left-1 > len(max_s):
                        max_s = s[left+1:right]
                    break
                left -= 1
                right += 1 
            
            mid += 1    
        return max_s


s = "babad"
s = "cbbd"
s = 'aaaa'
out = longestPalindrome(s)



























