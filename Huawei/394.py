# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 09:01:44 2021

@author: Lenovo
"""

def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    def find_front_end(s):
        if s == '':
            return 0, 0, False
        stack = []
        contain = False
        for i in range(len(s)):
            if s[i] == '[':
                contain = True
                if stack == []:
                    front = i
                stack.append(s[i])
            if s[i] == ']':
                stack.pop()
                if stack == []:
                    end = i
                    break
        if not contain:
            front = 0
            end = len(s)-1
        return int(front), int(end), contain

    if s == '':
        return ''

    front, end, contain = find_front_end(s)
    if not contain:
        return s
    else:
        i = front -1
        nums = []
        while True:
            if i < 0:
                break
            if not s[i].isnumeric():
                break
            nums.insert(0, int(s[i]))
            i -= 1
        times = 0
        for i in range(len(nums)):
            times = times*10+nums[i]
        print(times)
        nexts = s[front+1: end]
        res = s[0:front-len(nums)] + times*decodeString(nexts) + decodeString(s[end+1::])
        return res



s = "3[a2[c]]"
res = decodeString(s)



