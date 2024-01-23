class Empty(Exception):
    pass

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None


class Queue:
    def __init__(self):
        self._first = None
        self._n = 0
    
    def isEmpty(self):
        return self._n == 0
    
    def __len__(self):
        return self._n
    
    def top(self):
        if self._n == 0:
            raise Empty("Empty")
        return self._first._data
    
    def enqueue(self, data):
        node = Node(data)
        if self._n == 0:
            self._first = node
        else:
            curr = self._first
            while curr._next != None:
                curr = curr._next
            curr._next = node
        self._n += 1

    def dequeue(self):
        if self._n == 0:
            raise Empty("Empty")
        value = self._first._data
        self._first = self._first._next
        return value
    
q = Queue()
q.enqueue(54)
q.enqueue(64)
q.enqueue(3424)
q.enqueue(1)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())



     