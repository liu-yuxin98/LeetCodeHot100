# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 08:53:21 2021

@author: Lenovo
"""
class TrieNode:

    def __init__(self, value):
        self.value = value
        self.child = []*26



def minimumLengthEncoding(words):
    """
    :type words: List[str]
    :rtype: int
    """
    def move(words):
        i = 0
        while True:
            if i >= len(words):
                break
            j = i+1
            while j < len(words):
                if words[i] in words[j]:
                    if words[i] == words[j][len(words[j])-len(words[i]):len(words[j])]:
                        words.pop(i)
                        i -= 1
                        break
                if words[j] in words[i]:
                    if words[j] == words[i][len(words[i])-len(words[j]):len(words[i])]:
                        words.pop(j)
                        j -= 1
                j += 1
            i += 1
    move(words)
    print(words)
    s = '#'.join(words)
    s += '#'
    return s

words = ["me", 'ti', "time",  "bell", 'times']
words = ['a','abcd','bc','bcdef','ef','ab','cd','h','def']
words = ["feipyxx","e"]

s = minimumLengthEncoding(words)
            

        
        
    
