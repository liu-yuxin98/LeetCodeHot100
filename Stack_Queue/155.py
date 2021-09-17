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
        self.stack = []
        self.minvalue = None


    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.stack) == 0:
            self.stack.append(val)
            self.minvalue = val
        else:
            if self.minvalue <= val:
                self.stack.append(val)
            else:
                self.stack.append(2*val - self.minvalue)
                self.minvalue = val
        return 0


    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) != 0:
            if self.stack[-1] >= self.minvalue:
                self.stack.pop()
            

        

    def top(self):
        """
        :rtype: int
        """
        

    def getMin(self):
        """
        :rtype: int
        """