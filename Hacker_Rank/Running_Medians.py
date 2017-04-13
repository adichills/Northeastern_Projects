#!/bin/python

import sys


n = int(raw_input().strip())
a = []
a_i = 0
for a_i in xrange(n):
    a_t = int(raw_input().strip())
    a.append(a_t)

class max_heap:
    def __init__(self,items):
        self.items = []
        self.items.append(0)
        i = 1
        for e in items:
            self.items.append(e)
            self.floatUp(i)
            i=i+1
    
    def peek(self):
        if len(self.items)>1:
            return self.items[1]
  
    def push(self,item):
        self.items.append(item)
        self.floatUp(len(self.items)-1)
  
    def floatUp(self,index):
        parent = index//2
        if parent > 0:
            if self.items[parent]< self.items[index]:
                self.swap(parent,index)
                self.floatUp(parent)
  
    def bubbledown(self,index):
        larger = index
        leftchild = index * 2
        rightchild = leftchild +1 
        if leftchild < len(self.items):
            if self.items[leftchild] > self.items[index]:
                larger = leftchild
            if rightchild < len(self.items):
                if self.items[leftchild] < self.items[rightchild]:
                    larger = rightchild
        if larger !=index:
            self.swap(larger,index)
            self.bubbledown(larger)
  
    def pop(self):
        if len(self.items) <=1:
            return
        self.swap(1,len(self.items)-1)
        item = self.items.pop()
        self.bubbledown(1)
        return item
    
    def size(self):
        return len(self.items) - 1
  
    def swap(self,i,j):
        self.items[i],self.items[j] = self.items[j],self.items[i]

class min_heap:
    def __init__(self,items):
        self.items = []
        self.items.append(0)
        i = 1
        for e in items:
            self.items.append(e)
            self.floatUp(i)
            i=i+1
    
    def peek(self):
        if len(self.items)>1:
            return self.items[1]
  
    def push(self,item):
        self.items.append(item)
        self.floatUp(len(self.items)-1)
  
    def floatUp(self,index):
        parent = index//2
        if parent > 0:
            if self.items[parent] > self.items[index]:
                self.swap(parent,index)
                self.floatUp(parent)
  
    def bubbledown(self,index):
        larger = index
        leftchild = index * 2
        rightchild = leftchild +1 
        if leftchild < len(self.items):
            if self.items[leftchild] < self.items[index]:
                larger = leftchild
            if rightchild < len(self.items):
                if self.items[leftchild] > self.items[rightchild]:
                    larger = rightchild
        if larger !=index:
            self.swap(larger,index)
            self.bubbledown(larger)
  
    def pop(self):
        if len(self.items) <=1:
            return
        self.swap(1,len(self.items)-1)
        item = self.items.pop()
        self.bubbledown(1)
        return item
    
    def size(self):
        return len(self.items) - 1
  
    def swap(self,i,j):
        self.items[i],self.items[j] = self.items[j],self.items[i]



def avg_of_two_tops(a,b):
    return (a+b)*0.5

def calculate_running_median(cm,ne,max_h,min_h):
    if max_h.size() > min_h.size():
        if ne < cm:
            min_h.push(max_h.pop())
            max_h.push(ne)
        else:
            min_h.push(ne)
        return avg_of_two_tops(max_h.peek(),min_h.peek())
        
    elif max_h.size() < min_h.size():
        if ne > cm:
            max_h.push(min_h.pop())
            min_h.push(ne)
        else:
            max_h.push(ne)
        return avg_of_two_tops(max_h.peek(),min_h.peek())

    else:
        if ne < cm:
            max_h.push(ne)
            return max_h.peek() * 1.0
        else:
            min_h.push(ne)
            return min_h.peek() * 1.0

def print_running_median(a):
    l = max_heap([])
    r = min_heap([])
    cm = 0
    for e in a:
        cm = calculate_running_median(cm,e,l,r)
        print cm

print_running_median(a)
    
        