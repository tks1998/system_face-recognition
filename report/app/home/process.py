import os
import numpy as np
import heapq 

class Node:
    def __init__(self):
        self.index = -1 
        self.threshold = 0.0
        self.left = None
        self.right = None

class vptree:
    def __init__(self,maximum):
        self.items = np.arange(1,maximum+1) # create array 1->maximum+1 -> phan tu 0->10
        #print(self.items)
        self._tau = 10000000.00
        self.heap = []
        self.path = os.getcwd()+"\\home\\train\\"
    def distance(self,a,b):
        a1 = np.load(self.path+str(a)+".npy") # path
        a2 = np.load(self.path+str(b)+".npy")
        return np.linalg.norm(a1-a2)
        
    def _distance(self,a,b):
        a1 = np.load(self.path+str(a)+".npy") # path
        return np.linalg.norm(a1-b)
    def _partition(self,first,middle,last,key): # first -> last 
        #print(first,middle,last,key)
        (self.items[middle] , self.items[last]) = (self.items[last],self.items[middle])
        pivot = self.items[last]
        R = self.distance(pivot,key)
        i = first - 1 
        for j in range(first,last):
            if self.distance(self.items[j],key) < R:
                i= i+1
                (self.items[i],self.items[j])= (self.items[j],self.items[i])
        (self.items[i+1],self.items[last]) = (self.items[last], self.items[i+1])
        return (i+1)
    def build(self,lower,upper):
        if lower == upper:
            return None
        node = Node()
        node.index = lower 
        if upper-lower > 1:
            middle = round((lower+upper)/2)
            sp = self._partition(lower+1,middle,upper,self.items[lower])
            
            node.threshold = self.distance(self.items[lower],self.items[sp])

            node.index = lower
            node.left = self.build(lower+1,middle)
            node.right = self.build(middle+1,upper)
        return node 

    def search(self, node = None , target = [] , k = 0 ):
        if node == None:
            return 
        
        dist = self._distance(self.items[node.index],target)

        if dist < self._tau:
            if len(self.heap) == k:
                self.heap = heapq.nsmallest(len(self.heap)-1,self.heap,key = None)
                #heapq.heappop(self.heap)
            heapq.heappush(self.heap,(dist,self.items[node.index]))
            if len(self.heap) == k:
                self._tau = self.heap[len(self.heap)-1][0]  # get distance
        #print(self._tau)
        if node.left == None and node.right == None:
            return
        if dist<node.threshold:
            if dist-self._tau<=node.threshold:
                self.search(node.left,target,k)
            if dist+self._tau>=node.threshold:
                self.search(node.right,target,k)
        else:
            if dist+self._tau>=node.threshold:
                self.search(node.right,target,k)
            if dist-self._tau<=node.threshold:
                self.search(node.left,target,k)



