# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 11:45:01 2021

@author: Lenovo
"""


class Trie(object):

    class Node(object):
        def __init__(self, value):
            self.value = value
            self.child = [None]*26
            self.Is_word = False

        def Print_Node(self):
            print(self.value, self.Is_word)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = self.Node(0)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for i in range(len(word)):
            if p.child[ord(word[i])-ord('a')] is None:
                new_node = self.Node(word[i])
                p.child[ord(word[i])-ord('a')] = new_node
                p = new_node
            else:
                p = p.child[ord(word[i])-ord('a')]
            if i == len(word)-1:
                p.Is_word = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        temp = self.root
        for i in range(len(word)):
            if temp.child[ord(word[i])-ord('a')] is None:
                return False
            else:
                temp = temp.child[ord(word[i])-ord('a')]
        return temp.Is_word

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.root
        for i in range(len(prefix)):
            if p.child[ord(prefix[i]) - ord('a')] is None:
                return False
            else:
                p = p.child[ord(prefix[i]) - ord('a')]
        if p.Is_word:
            return True
        else:
            for node in p.child:
                if node is not None:
                    return True
            return False

    def print_trie(self, root):
        p = root
        p.Print_Node()
        for node in p.child:
            if node is not None:
                self.print_trie(node)

    def Print(self):
        self.print_trie(self.root)





