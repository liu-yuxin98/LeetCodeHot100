# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 20:28:54 2022

@author: yuxin_liu_1998
"""

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dic = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key in self.dic:
            n = self.dic[key]
            self._remove(n)
            self._add(n)
            return n.val
        return -1
    
    def put(self, key, value):
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key, value)
        self._add(n)
        self.dic[key] = n
        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]
    
    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p
    
    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

    def print_node(self):
        p = self.head
        while True:
            if p == None:
                break
            print(p.key)
            p = p.next
        print(self.dic)
        print('---------------')


# class Node:
#     def __init__(self,k,v):
#         self.key = k
#         self.value = v
#         self.pre = None
#         self.next = None
        
# class LRUCache:
        
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.key_dict = dict()
#         self.head = Node(0,0)
#         self.tail = Node(0,0)
#         self.head.next = self.tail
#         self.tail.prev = self.head
        
#     def get(self, key: int) -> int:
#         if key in self.key_dict:
#             node = self.key_dict[key]
#             self.remove_node(node)
#             self.insert_node(node)
#             return node.value       
#         return -1
    
#     def put(self, key: int, value: int) -> None:
#         if key in self.key_dict:
#             self.remove_node(self.key_dict[key])
#         node = Node(key,value)
#         self.insert_node(node)
#         self.key_dict[key] = node
#         if len(self.key_dict) > self.capacity:
#             node = self.head.next
#             self.remove_node(node)
#             del self.key_dict[node.key]
#             print('capacity full')

#     def remove_node(self,node):
#         p = node.pre
#         n = node.next
#         p.next = n
#         n.pre = p
        
#     def insert_node(self,node):
#         p = self.tail.prev
#         p.next = node
#         self.tail.prev = node
#         node.prev = p
#         node.next = self.tail
                
#     def print_node(self):
#         p = self.head
#         while True:
#             if p == None:
#                 break
#             print(p.key)
#             p = p.next
#         print(self.key_dict)
#         print('---------------')
        
    
        
        
        



                    
                
                
lRUCache =  LRUCache(2);
lRUCache.put(1, 1) # cache is {1=1}

lRUCache.print_node()
lRUCache.put(2, 2) # cache is {1=1, 2=2}
lRUCache.print_node()

lRUCache.get(1)    # return 1
lRUCache.print_node()

lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.print_node()

x = lRUCache.get(2)   #  returns -1 (not found)
lRUCache.print_node()

x = lRUCache.get(1)
lRUCache.print_node()

lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.print_node()

lRUCache.get(1)  # return -1 (not found)
lRUCache.print_node()

lRUCache.get(3)   # return 3
lRUCache.print_node()

lRUCache.get(4) # return 4 
lRUCache.print_node()

       
