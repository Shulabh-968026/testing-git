#! /usr/bin/python3
class Stack:
    def __init__(self,size=5):
        self.size = size
        self.stack = []
    
    def isEmpty(self):
        if self.size == len(self.stack):
            return False
        else:
            return True
