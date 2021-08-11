# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:06:07 2021

@author: Lenovo
"""

# one line input

def load_box(box):
    # sort
    box = [[max(b[0], b[1]), min(b[0], b[1])] for b in box]
    box.sort(key=lambda x: [x[0], x[1]], reverse= True)
    # iterate through
    layer = 1
    for i in range(len(box)-1):
        if max(box[i]) >= max(box[i+1]) and min(box[i]) >= min(box[i+1]):
            layer += 1
    return layer


box = eval(input().strip())
if len(box) <= 0:
    print(0)
else:
    box = [[max(b[0], b[1]), min(b[0], b[1])] for b in box]
    box.sort(key=lambda x: [x[0], x[1]], reverse= True)
    layer = 1
    for i in range(len(box)-1):
        if max(box[i]) >= max(box[i+1]) and min(box[i]) >= min(box[i+1]):
            layer += 1
    print(layer)

