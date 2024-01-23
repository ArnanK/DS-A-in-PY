class Empty(Exception):
    pass

class Stack:
    def __init__(self):
        self._A = []
        self._n = 0

    def isEmpty(self):
        return self._n == 0
    
    def __len__(self):
        return self._n
    
    def push(self, data):
        self._A.append(data)
        self._n += 1
    
    def pop(self):
        if self._n == 0:
            raise Empty("Is empty")
        self._n -= 1
        return self._A.pop()
    
    def top(self):
        if self._n == 0:
            raise Empty("Is empty")
        return self._A[-1]
    
