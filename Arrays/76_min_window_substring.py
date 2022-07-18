# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 17:31:25 2022

@author: yuxin_liu_1998
"""


# sol 1 using dict to store char info
def minWindow(s: str, t: str) -> str:
        # initial lization t_dict,
        # t_dict record the exceeds numbers of char for s[start:end+1] to conatin all char in t
        # if t_dict[a] = -1 means , lack 1 number of a in s[start:end+1]
        # if t_dict[a] = 0 means, s[start:end+1] conatin exactly number of 'a' in t
        t_dict = {}
        for char in t:
            t_dict[char] = t_dict.get(char,0) - 1
        
        best = s[0::]
        start = 0
        end = 0
        find = False
        
        # iterate while not reach the end of s
        while end<len(s):
            if s[end] in t:
                t_dict[s[end]] += 1
                # decide if the [start,end] contain all character in t
                for char in t_dict:
                    if t_dict[char] < 0:
                        break # char does not included in s[start:end+1]
                else:
                    find = True
                    # s[start:end+1] conatins all char in t
                    # move start forward till s[start:end+1] does not contain all char in t
                    while start <= end:
                        if s[start] in t_dict:
                            t_dict[s[start]] -= 1
                            if t_dict[s[start]] < 0: # we can not move start forward 
                                if end-start+1 <=len(best):
                                    best = s[start:end+1]
                                    if len(best) == len(t): # already the best
                                        return best
                                start += 1
                                break
                        # move start forward
                        start += 1
            # move end backward till find all char in t
            end += 1        
        if find:
            return best
        return ""


# sol2 headdict store char info
def minWindow(s: str, t: str) -> str:
        # initial lization t_dict,
        # t_dict record the exceeds numbers of char for s[start:end+1] to conatin all char in t
        # if t_dict[a] = -1 means , lack 1 number of a in s[start:end+1]
        # if t_dict[a] = 0 means, s[start:end+1] conatin exactly number of 'a' in t
        
        import heapdict  # it is not supported in leetcode
        t_dict = heapdict.heapdict()
        for char in t:
            t_dict[char] = t_dict.get(char,0) - 1
            
        best = s[0::]
        start = 0
        end = 0
        find = False
        
        # iterate while not reach the end of s
        while end<len(s):
            if s[end] in t:
                t_dict[s[end]] += 1
                # decide if the [start,end] contain all character in t
                if t_dict.peekitem()[1] >= 0:
                    find = True
                    # s[start:end+1] conatins all char in t
                    # move start forward till s[start:end+1] does not contain all char in t
                    while start <= end:
                        if s[start] in t_dict:
                            t_dict[s[start]] -= 1
                            if t_dict[s[start]] < 0: # we can not move start forward 
                                if end-start+1 <=len(best):
                                    best = s[start:end+1]
                                    if len(best) == len(t): # already the best
                                        return best
                                start += 1
                                break
                        # move start forward
                        start += 1
            # move end backward till find all char in t
            end += 1        
        if find:
            return best
        return ""



s = "ADOBECODEBANC"
t = "ABC"

# s = "A"
# t = "ABC"


# s = "A"
# t = "A"

# s = "abc"
# t = "ac"

out = minWindow(s,t)

















