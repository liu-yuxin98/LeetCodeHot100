# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 15:00:51 2021

@author: Lenovo
"""

N = eval(input())

all_values = []
for i in range(N):
    s = input().split()
    values = [eval(num) for num in s[1::]]
    values.append(s[0])
    all_values.append(values)

all_values.sort(key=lambda x: (x[0], x[1], x[2], x[3]))
country = []

for item in all_values:
    country.append(item[-1])
country = country[::-1]
for c in country:
    print(c)
    


