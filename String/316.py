# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 00:38:02 2021

@author: Lenovo
"""


# 单调栈
def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """

    stack = []
    for i in range(len(s)):
        if i == len(s)-1:
            if s[i] not in stack:
                stack.append(s[i])
        else:
            # 判断当前字符是否已经在栈里面了
            if s[i] not in stack:
                j = len(stack)-1
                # 遍历栈中元素，检查是否有调整的空间
                while True:
                    if j < 0:
                        break
                    if ord(stack[j]) < ord(s[i]):
                        break
                    else:
                        if stack[j] in s[i+1::]:
                            stack.pop(j)
                        else:
                            break
                    j -= 1
                stack.append(s[i])
        print(i, stack)
    return ''.join(stack)



def removeDuplicateLetters(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    pos = 0  # 记录一个pos，这个pos表明，stack[0:pos]已经实现最优情况，不能再改了
    for i in range(len(s)):
        if s[i] not in stack:
            j = len(stack)-1
            while j >= pos and ord(s[i]) < ord(stack[j]) and i != len(s)-1:
                if stack[j] in s[i+1::]:
                    stack.pop(j)
                else:
                    pos = j
                    break
                j -= 1
            stack.append(s[i])
    return ''.join(stack)

s = "cbacdcbc"
print(removeDuplicateLetters(s))