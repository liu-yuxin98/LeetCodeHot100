# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 23:58:17 2021

@author: Lenovo
"""


def numRabbits(answers):
    """
    :type answers: List[int]
    :rtype: int
    """
    color_dict = dict()
    for i in range(len(answers)):
        color_dict[answers[i]] = color_dict.get(answers[i], []) + [answers[i]]
    rabbits = 0
    for key in color_dict:
        new_color = len(color_dict[key])//(key+1)
        if len(color_dict[key])%(key+1):
            new_color += 1
        new_rabbits = (key+1)*new_color
        rabbits += new_rabbits
    return int(rabbits)



answers = [1, 1, 2]
rabbits = numRabbits(answers)
