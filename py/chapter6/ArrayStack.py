class Empty(Exception):
    pass

# The `ArrayStack` class is an implementation of a stack data structure using an array.
class ArrayStack:
    def __init__(self):
        self._data=[]
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data)==0
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty(): 
            raise Empty('Stack is Empty')
        return self._data[len(self._data)-1]
    
    def pop(self):
        if(self.is_empty()): 
            raise Empty('Stack is Empty')
        return self._data.pop()



#  Stack 
def isMatched(c):
    """
    The function checks if a given string of characters has matching opening and closing brackets.
    
    :param c: The parameter `c` is a string that represents a sequence of characters
    :return: a boolean value. It returns True if the input string `c` contains matching pairs of opening
    and closing brackets (i.e., `{}`, `[]`, `()`), and False otherwise.
    """
    right='}])'
    left ='{[('
    stack = ArrayStack()
    for n in c:
        if n in left:
            stack.push(n)
        elif n in right:
            if stack.is_empty():
                return False
            if right.index(n) != left.index(stack.pop()):
                return False
    return stack.is_empty()

def isMatchedHTML(raw):
    S = ArrayStack()
    j = raw.find('<')
    while j != -1:
        k = raw.find('>', j+1)
        if k == -1:
            return False
        tag = raw[j+1,k]
        if not tag[0] == '/':
            S.push(tag)
        else:
            if S.is_empty:
                return False
            if tag[1:] != S.pop():
                return False
        j=raw.find('<', k+1)
    return S.is_empty()

def recursiveRemove(s:ArrayStack):
    if s.is_empty():
        return None
    else:
        s.pop()
        recursiveRemove(s)
    




s = ArrayStack()
s.push(5)
s.push(6)
s.push(7)
s.push(8)
print(len(s))
recursiveRemove(s)
print(len(s))


