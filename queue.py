#! /usr/bin/python3

class Queue:
    def __init__(self,size=5):
        self.size = size
        self.queue = []
    
    def isEmpty(self):
        if len(self.queue) == self.size:
            return False
        else:
            return True

    def push(self,val):
        if self.isEmpty():
            self.queue.append(val)
        else:
            print("Queue is overflow!!")

