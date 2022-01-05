# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 11:46:29 2021

@author: Lenovo
"""

class StockSpanner(object):

    def __init__(self):
        self.price = []
        self.stack = []


    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        self.price.append(price)

        while True: 
            if self.stack == []:
                self.stack.append(len(self.price)-1)
                return len(self.price)
            elif self.price[-1] < self.price[self.stack[-1]]:
                span = len(self.price)-1-self.stack[-1]
                self.stack.append(len(self.price)-1)
                return span
            else:
                self.stack.pop()
            
        
    

        