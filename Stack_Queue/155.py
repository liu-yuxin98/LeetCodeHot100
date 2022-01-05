# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 23:50:27 2021

@author: Lenovo
"""

class MinStack(object):
    
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        import sys
        self.stack = []
        self.minvalue = sys.maxsize


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        self.minvalue = min(val,self.minvalue)     




    def pop(self):
        """
        :rtype: None
        """
        value = self.stack.pop()
        if value == self.minvalue:
            if self.stack != []:
                self.minvalue = min(self.stack)
            else:
                self.minvalue = 'null'
        return value

            

        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minvalue

'''
["MinStack","push","push","push","top","pop","getMin","pop","getMin","pop","push","top","getMin","push","top","getMin","pop","getMin"]
[[],[2147483646],[2147483646],[2147483647],[],[],[],[],[],[],[2147483647],[],[],[-2147483648],[],[],[],[]]
'''
obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483646)
obj.top()

print(type(''))