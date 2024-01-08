import ctypes

# The `DynamicArray` class is an implementation of a dynamic array data structure in Python, which
# allows for efficient resizing and manipulation of an array-like sequence.
class DynamicArray:
    def __init__(self):
        self._n=0
        self._capacity=1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('Invalid Index')
        return self._A[k]
    
    def isEmpty(self):
        return self._n == 0

    def insert(self,k,value):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for j in range(self._n, k, -1):
            self.A[j] = self.A[j-1]
        self._A[k]=value
        self._n+=1
    
    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k,self._n-1):
                    self._A[j] = self._A[j+1] 
                self._A[self._n-1] = None
                self._n -=1
                if float(self._n / self._capacity) <= 0.25:
                    self._resize(self._capacity//2)
                return
        raise ValueError('Value not found')

    def delete(self, index):
        if 0 <= index < self._n:
            for j in range(index, self._n-1, 1):
                self._A[j] = self._A[j+1]
            self._A[self._n] = None
            self._n-=1
            if float(self._n / self._capacity) <= 0.25:
                self._resize(self._capacity//2)
            return
        else: 
            raise IndexError('Index not found')
        

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n +=1
    
    def prepend(self,obj):
        if self._n == self._capacity:
            self._resize(2*self._capacity)
        for k in range(self._n, 0, -1):
            self._A[k] = self._A[k-1]
        self._A[0]=obj
        self._n+=1

    def printSequence(self):
        for i in range(self._n):
            print(self._A[i], end=" ")
        print()  # Print a newline after the sequence

    def _resize(self,c):
        B=self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def _make_array(self,c):
        a = [None] * c
        return a
    
    
    


            
            

        

arr = DynamicArray()
print(arr.isEmpty())
arr.prepend(1)
print(arr.isEmpty())
arr.append(2)
arr.append(3)
arr.append(4)
arr.append(5)
arr.append(6)
arr.append(7)
arr.append(8)
arr.append(9)
arr.append(10)
arr.append(11)
arr.prepend(4)
arr.printSequence()
arr.delete(5)
arr.printSequence()

