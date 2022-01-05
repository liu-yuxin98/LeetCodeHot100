# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 12:15:01 2021

@author: Lenovo
"""

def removeKdigits( num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <= k:
            return '0'
        num = list(num)
        drop = 0
        while True:
            if drop >= k:
                break
            index = 1

            while True:
                if index >= len(num):
                    num.pop()
                    drop += 1
                    break
                if num[index] < num[0]:
                    num = num[1::]
                    drop += 1
                    break
                elif num[index] == num[index-1]:
                    index += 1
                elif num[index] > num[index-1]:
                    if index == len(num)-1:
                        drop += 1
                        num.pop()
                        break
                    elif num[index] >= num[index+1]:
                        drop += 1
                        del num[index]
                        break
                    else:
                        index += 1
            
            j = 0
            while j < len(num) and num[j]=='0':
               j += 1
            num = num[j::] 
            if num == []:
                return '0'                        

        return ''.join(num)



def removeKdigits( num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        remain = len(num) - k
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        return ''.join(stack[:remain]).lstrip('0') or '0'

def removeKdigits( num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []
        remain = len(num) - k
        for digit in num:
            while True:
                if k <= 0:
                    break
                if stack == []:
                    break
                elif stack[-1] > digit:
                    stack.pop()
                    k -= 1
                    break
            stack.append(digit)
        
        return ''.join(stack[:remain]).lstrip('0') or '0'
        


num = "1432219"
k = 3
num = "123456"
k = 3
num = "10"
k = 2
num = "10200"
k = 1
res = removeKdigits(num, k)   