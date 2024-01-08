class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self) -> None:
        self._header = self._Node(None,None,None)
        self._trailer = self._Node(None,None,None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, e, predecessor, successor):
        x = self._Node(e, predecessor, successor)
        predecessor._next = x
        successor._prev = x
        self._size += 1
        return x
    
    def _delete_node(self,node):
        pred = node._prev
        succ = node._next

        pred._next = succ
        succ._prev = pred
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None #delete node from mem
        return element