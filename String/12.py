# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:53:21 2021

@author: Lenovo
"""

def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    num_pair = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX',
                10: 'X', 40: 'XL', 50: 'L', 90: 'XC',
                100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    output = ''
    # 1000 <= num
    while True:
        if num < 1000:
            break
        num = num - 1000
        output += num_pair[1000]
    # 900 <= num < 1000
    if 900 <= num < 1000:
        num -= 900
        output += num_pair[900]
    # 500 <= num < 900
    if 500 <= num < 900:
        num -= 500
        output += num_pair[500]
    # 400 <= num < 500
    if 400 <= num < 500:
        num -= 400
        output += num_pair[400]
    # 100 <= num < 400
    while True:
        if num < 100:
            break
        num -= 100
        output += num_pair[100]
    # 90 <= num < 100
    if 90 <= num < 100:
        num -= 90
        output += num_pair[90]
    # 50 <= num < 90
    if 50 <= num < 90:
        num -= 50
        output += num_pair[50]
    # 40 <= num < 50
    if 40 <= num < 50:
        num -= 40
        output += num_pair[40]
    # 10 <= num < 40
    while True:
        if num < 10:
            break
        num -= 10
        output += num_pair[10]
    # num == 9
    if num == 9:
        num -= 9
        output += num_pair[9]
    # 5 <= num < 9
    if 5 <= num < 9:
        num -= 5
        output += num_pair[5]
    #  num == 4
    if num == 4:
        num -= 4
        output += num_pair[4]
    # 0 <= num < 4
    while True:
        if num <= 0:
            break
        num -= 1
        output += num_pair[1]

    return output

def intToRoman(num):
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romans = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
    output = ''
    while True:
        if num <= 0:
            break
        for i in range(len(values)):
            if num >= values[i]:
                num -= values[i]
                output += romans[i]
                break
    return output



output  = intToRoman(3)
