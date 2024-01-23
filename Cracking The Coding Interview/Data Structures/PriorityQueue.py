class Empty(Exception):
    pass

class PriorityQueue:
    def __init__(self):
        self._capacity = 10
        self._n = 0
        self._A = [None] * self._capacity
        

    def insert(self, value):
        self._n += 1
        if (self._n) >= self._capacity:
            self._capacity = self._capacity * 2
            self._resizeArray(self._capacity)
        self._A[self._n] = value
        self._percolateUp(self._n)
        

    def deleteMin(self):
        if self._n == 1:
            raise Empty("There are no values within the Priority Queue")
        value = self._A[1]
        self._A[1] = self._A[self._n]
        self._n -= 1
        self._percolateDown(1)
        return value
    
    def _percolateUp(self, index):
        value = self._A[index]
        while index > 1 and self._A[(index ) // 2] > value:
            self._A[index] = self._A[(index ) // 2]
            index = (index ) // 2
        self._A[index] = value

    
    def _percolateDown(self, index):
        pass


    def _resizeArray(self, newCapacity):
        b = [None] * newCapacity
        for i in range(self._n):
            b[i] = self._A[i]
        self._A = b
        self._capacity = newCapacity

p = PriorityQueue()
p.insert(4)
p.insert(1)
p.insert(2)
p.insert(43)
p.insert(2)
p.insert(20)
p.insert(3)

print(p._A)