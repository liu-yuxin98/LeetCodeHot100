# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:51:48 2022

@author: yuxin_liu_1998
"""

def lengthOfLongestSubstring(s: str) -> int:
        front = 0
        end = 0
        max_length = 0        
        char_dict = set()
    
        while end<len(s):
            # find replication
            if s[end] in char_dict:
                max_length = max(max_length, end-front)
                # move front till meet the replicated char
                while front<end:
                    if s[front] == s[end]:
                        front +=1
                        break
                    # remove item from set
                    char_dict.remove(s[front])
                    front += 1
            else:
                char_dict.add(s[end])    
            end += 1
        return max(max_length,end-front)

s = ""
s ="1"
s = "111"
s = "pwwkew"
s = 'cccccc'
s = 'abcabcbb' 
s = "1234"
s = "tmmzuxt"
out = lengthOfLongestSubstring(s)
print(out)
