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

    def push(self,val):
        if self.isEmpty():
            self.stack.append(val)
        else:
            print("Stack is Overflow!!")

    def pop(self):
        if self.isEmpty():
            print("Stack is underflow!!")
        else:
            self.stack.pop()

    def top(self):
        if self.isEmpty():
            print("Stack is underflow!!")
        else:
            print(f"top value of stack::{self.stack[-1]}")
