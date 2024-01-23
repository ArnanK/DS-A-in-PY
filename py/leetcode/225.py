from _collections import deque

class MyStack:
    def __init__(self):
        self._A = deque()
        self._n = 0

    def push(self, x):
        self._A.append(x)
        i = 0 
        while i < self._n:
            self._A.append(self._A.popleft())
            i+=1

    def pop(self):
        if self._A:
            self._n -=1
            return self._A.popleft()

    def top(self):
        if self._A:
            return self._A[0]

    def empty(self):
        if self._A:
            return False
        return True


obj = MyStack()
obj.push(1)
obj.push(2)
print(obj._A)