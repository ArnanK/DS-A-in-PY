class Empty(Exception):
    pass

class ArrayList:
    def __init__(self):
        self._capacity = 11
        self._A = [None] * self._capacity
        self._n = 0

    def __len__(self):
        return self._n
    
    def isEmpty(self):
        return self._n == 0 
    
    def _resizeArray(self, newCapacity):
        b = [None] * newCapacity
        for i in range(self._n):
            b[i] = self._A[i]
        self._A = b
        self._capacity = newCapacity

    def append(self, data):
        if self._n >= self._capacity:
            self._resizeArray(self._capacity * 2)
        self._A[self._n] = data
        self._n += 1
        
    def insert(self, index, data):
        if self._n >= self._capacity:
            
            self._resizeArray(self._capacity * 2)
        i = self._n
        while i > index:
            self._A[i] = self._A[i-1]
            i -= 1
        self._A[index] = data
        self._n += 1

    def remove(self, index):
        if self.isEmpty(): 
            raise Empty('Array is empty!')
        if 0 <= index < self._n:
            i = index
            while i < self._n-1:
                self._A[i] = self._A[i+1]
                i += 1
            self._A[i] = None
            self._n -= 1
            if self._n / self._capacity < 0.5:
                self._resizeArray(self._capacity//2)

        else:
            raise IndexError('Not Valid Index')


    def printArray(self):
        for i in range(self._n):
            print(self._A[i], end=" ")
        print()

a = ArrayList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)
a.remove(0)
a.remove(0)
a.remove(0)
a.remove(0)
a.remove(0)
a.remove(0)




a.printArray()
print(a._capacity)