class Empty(Exception):
    pass

class Node:
    def __init__(self, data):
        self._data = data
        self._next = None

class LinkedList:    
    def __init__(self):
        self._first = None
        self._last = None
        self._n = 0

    def __len__(self):
        return self._n

    def is_empty(self):
        return self._n == 0

    def append(self, data):
        newNode = Node(data)
        if self._n == 0:
            self._first = newNode
            self._last = newNode
        else:
            self._last._next = newNode
            self._last = newNode
        self._n += 1

    def prepend(self,data):
        newNode = Node(data)
        if self._n == 0:
            self._first = newNode
            self._last = newNode
        else:
            newNode._next = self._first
            self._first = newNode
        self._n += 1

    def insert(self, index , data):
        if 0 <= index < self._n:
            if index == 0:
                self.prepend(data)
            elif index == self._n -1:
                self.append(data)
            else:
                curr = self._first
                prev = curr
                newNode = Node(data)
                i = 0
                while i < index:
                    prev = curr
                    curr = curr._next
                    i+=1
                prev._next = newNode
                newNode._next = curr._next
                self._n += 1
        else:
            raise IndexError("Not valid index")
  

    def remove(self, data):
        if self.is_empty():
            raise Empty('Linked List is empty!')
        curr = self._first
        prev = curr

        for i in range(self._n-1):
            if data == curr._data:
                break
            prev = curr
            curr = curr._next
 
        if data != curr._data:
            raise ValueError('Value not inside Linked List')

        if curr == self._first:
            self._first = curr._next
            curr = None
            self._n -=1
        else:
            if curr == self._last:
                self._last = prev
            prev._next = curr._next
            self._n -=1
        
            

    def print_sequence(self):
        if self.is_empty():
            raise Empty('Linked List is empty!')
        curr = self._first

        while curr is not None:
            print(curr._data, end=' ')
            curr = curr._next

a = LinkedList()
a.append(2)
a.prepend(1)
a.append(2)
a.append(3)
a.append(5)
a.insert(4,4)
a.remove(3)


a.print_sequence()
print()
print(a._last._data)
