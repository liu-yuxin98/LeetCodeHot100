# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 18:42:57 2021

@author: Lenovo
"""


N = 2
M = 8
cave = [0,-1,-1,-2,-1,-3,-2,-4,-1,0]
cave = [0,-1,-2,0]


N = eval(input())
M = int(input())
cave = eval(input())

length_dict = {}
trace_dict = {}

for i in range(len(cave)):
    if cave[i] >= 0:
        for key in trace_dict:
            if key in length_dict:
                if trace_dict[key] > 0:
                    length_dict[key].append(trace_dict[key])
            else:
                if trace_dict[key] > 0:
                    length_dict[key] = [trace_dict[key]]
                else:
                    length_dict[key] = []
            trace_dict[key] = 0

    else:
        if cave[i] in trace_dict:
            trace_dict[cave[i]] += 1
        else:
            trace_dict[cave[i]] = 1

        for key in trace_dict:
            if key == cave[i]:
                continue
            else:
                if key > cave[i]:
                    trace_dict[key] += 1
                else:  # key < cave[i]
                    if key not in length_dict:
                        length_dict[key] = [trace_dict[key]]
                    else:
                        length_dict[key].append(trace_dict[key])
                    trace_dict[key] = 0

total = 0
for key in length_dict:
    len_list = length_dict[key]
    nums = sum([length//N for length in len_list])
    total += nums

print(total)





