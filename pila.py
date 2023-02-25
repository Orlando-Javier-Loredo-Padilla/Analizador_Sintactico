# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:27:14 2023

@author: Orlando
"""


class Stack:
    items = []
    def __init__(self):
        self.items = []

        self.push(2)
        self.push(0)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(len(self.items),item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def mostrarPila(self):
        for dato in self.items:
            print(str(dato), end=" ")
        print("                  ", end ="")
        #print()
        

class Stack2:
    items = []
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(len(self.items),item)

    def pop(self):
        if len(self.items) > 1:
         return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)
    
    
    def clear(self):
        self.items.clear()

    def mostrar_entrada(self):
        for dato in self.items:
            print(str(dato), end=" ")
        print()
        
class Stack3:
    items = []
    def __init__(self):
        self.items = []

        self.push(2)
        self.push(0)

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(len(self.items),item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

    def mostrarPila(self):
        for dato in self.items:
            print(str(dato), end=" ")
        print("                                     ", end ="")
        
        

class Stack4:
    items = []
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(len(self.items),item)

    def pop(self):
        if len(self.items) > 1:
         return self.items.pop(0)

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)
    
    
    def clear(self):
        self.items.clear()

    def mostrar_entrada(self):
        for dato in self.items:
            print(str(dato), end=" ")
        print()