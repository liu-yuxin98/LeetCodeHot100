# -*- coding: utf-8 -*-
"""
Created on Wed May  5 19:13:23 2021

@author: Liuyuxin
"""
def countBits(num):
        bits = [0]
        highBit = 0
        for i in range(1, num + 1):
            if i & (i - 1) == 0:
                highBit = i
            bits.append(bits[i - highBit] + 1)
        return bits


