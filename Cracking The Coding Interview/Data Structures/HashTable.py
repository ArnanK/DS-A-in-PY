class Node:
    def __init__(self, key, value):
        self._key = key
        self._value = value
        self._next = None


class HashMap:
    """
    Need Key and use a hash function to determine which
    index within array to insert into.

    """
    LOAD_FACTOR = 1.0
    def __init__(self):
       self._n = 0
       self._m = 11
       self._A = [None] * self._m

    def _hashFucntion(self,key):
        return hash(key) % self._m
    
    def exists(self, key):
        index = self._hashFucntion(key)
        if self._A[index] is None:
            return False
        curr = self._A[index]
        while curr is not None:
            if curr._key == key:
                return True
            curr= curr._next
        return False

    def get(self,key):
        index = self._hashFucntion(key)
        values = []
        if self._A[index] is None:
            return values
        curr = self._A[index]
        while curr is not None:
            if curr._key == key:
                values.append(curr._value)
            curr= curr._next
        return values

    def remove(self, key):
        index = self._hashFucntion(key)
        if self._A[index] is None:
            return "Empty"
        curr = self._A[index]
        prev = None
        while curr is not None:
            if curr._key == key:
                if prev:
                    prev._next = curr._next
                    curr = None
                else:
                    self._A[index] = curr._next
                return 
            
            prev = curr
            curr= curr._next

    def printMap(self):
        for i in range(self._m):
               print(f"{i}: ", end=' ')
               self._print_sequence(i)


    def _print_sequence(self, index):
        curr = self._A[index]

        while curr is not None:
            print(curr._value, end=' ')
            curr = curr._next
        print()

    def _resizeArray(self, newCapacity):
        b = [None] * newCapacity
        for i in range(self._n):
            b[i] = self._A[i]
        self._A = b
        self._m = newCapacity

    def _checkLoadFactor(self):
        if (self._n+1) / self._m > 1.0:
            self._resizeArray(self._m*2)

    def insert(self, key, value):
        self._checkLoadFactor()
        index = self._hashFucntion(key)
        node = Node(key, value)

        if self._A[index] is None:
            self._A[index] = node
        else:
            curr = self._A[index]
            while curr._next is not None:
                curr = curr._next
            curr._next = node
        self._n += 1



h = HashMap()
h.insert(0,1)
h.insert(1,2)
h.insert(2,3)
h.insert(3,4)
h.insert(4,5)
h.insert(5,6)
h.insert(6,7)
h.insert(1231231237,4)
h.insert(8,4)
h.insert(93453453,4)
h.insert(1543450,4)
h.insert(15435341,123)
h.insert(132422,234)
h.insert(1123123,543)
h.insert(14353454,654)
h.insert(7234,4)
h.insert(342342348,4)
h.insert(9,4)
h.insert(10,4)
h.insert(12341,123)
h.insert(11232,234)
h.insert(13453453,543)
h.insert(12342344,654)
h.printMap()