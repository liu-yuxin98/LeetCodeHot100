# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 18:52:51 2021

@author: Lenovo
"""

def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
        return 'Zero'
    values = [1000000000, 1000000, 1000, 100]

    values2 = [ 90, 80, 70, 60, 50, 40, 30, 20,
              19, 18, 17, 16, 15, 14, 13, 12, 11, 10,
              9, 8, 7, 6, 5, 4, 3, 2, 1]

    names = ['Billion', 'Million', 'Thousand', 'Hundred']

    names2 = ['Ninety', 'Eighty', 'Seventy', 'Sixty', 'Fifty', 'Forty', 'Thirty', 'Twenty',
              'Nineteen', 'Eighteen',  'Seventeen',  'Sixteen', 'Fifteen', 'Fourteen', 'Thirteen', 'Twelve', 'Eleven', 
              'Ten', 'Nine', 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two', 'One']
    output = ''

    for i in range(4):
        if num >= values[i]:
            coef = num // values[i]
            num = num % values[i]
            coef_name = numberToWords(coef)
            output += ' '+ coef_name + ' ' + names[i]

    while True:
        if num <= 0:
            break
        for i in range(len(values2)):
            if num >= values2[i]:
                num -= values2[i]
                output += ' ' + names2[i]
                break
    output = output.strip()
    return output

num = 1234567891
s = numberToWords(num)

