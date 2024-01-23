import math


def isUnique(string: str) -> bool:
    lst = list(string)
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return False
    return True

def checkPermutation(a:str, b:str) -> bool:
    if len(a) != len(b):
        return False
    lsta = list(a)
    lstb = list(b)

    lsta.sort()
    lstb.sort()
    for i in range(len(lsta)):
        if lsta[i] != lstb[i]:
            return False
    
    return True
    
"""
Iterate through str
    If chr is space:
        if next chr is not space:
            replace the space with '%20'
    
    remove all spaces
    return str
"""
def URLify(string: str) -> str:
    string = string.strip()
    string = string.replace(" ", "%20")
    return string

def URLify2(string: str, n:int) -> str:
    lst = list(string)
    i = 0
    while i < n:
        if lst[i] != ' ':
            break 
        lst.pop(i)
        i+=1
    j = n-1
    while j >= 0:
        if lst[j] != ' ':
            break
        lst.pop(j)
        j-=1
    

    for i in range(len(lst)-1):
        if lst[i] == " " and lst[i+1] != " ":
            lst[i] = "%20"
    string = ""
    return string.join(lst)

def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    l1 = len(str1)
    l2 = len(str2)
    n = math.gcd(l1,l2)
    a = b = n
    GCDArray = [None] * n
    GCDString = ""
    i = 0
    while i < n:
        if str1[i] == str2[i]:
            GCDArray[i] = str1[i]
        else:
            return ""
        i+=1
    while a < l1:
        if GCDArray[a%n] != str1[a]:
            return ""
        a+=1
    
    while b < l2:
        if GCDArray[b%n] != str2[b]:
            return ""
        b+=1
        
    return GCDString.join(GCDArray)


def reverseVowels(s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        stack = []
        
        for i in range(len(s)):
            if s[i] in vowels:
                stack.append(s[i])
        lst = list(s)

        for i in range(len(lst)):
            if lst[i] in vowels:
                lst[i] = stack.pop()
        
        
        return "".join(lst)
        


print(reverseVowels("hello"))