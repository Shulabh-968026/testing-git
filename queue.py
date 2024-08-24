#! /usr/bin/python3

class Queue:
    def __init__(self,size=5):
        self.size = size
        self.queue = []
<<<<<<< HEAD
=======
    
    def isEmpty(self):
        if len(self.queue) == self.size:
            return False
        else:
            return True
>>>>>>> f331a52 (fix: add queue and update stack)
