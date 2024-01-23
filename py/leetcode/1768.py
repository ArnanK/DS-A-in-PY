word1="ab"
word2="pqrs"

def mergeAlternatively(word1:str, word2:str) ->str:
    n = min(word1, word2)
    n = len(n)
    merge=""
    for i in range(n):
        if word1[i]:
            merge += word1[i]
        if word2[i]:
            merge += word2[i]
    
    m = max(word1, word2)
    
    if len(word1) > len(word2):
        while n < len(m):
            merge += word1[n]
            n += 1
    else:
        while n < len(m):
            merge += word2[n]
            n += 1
            
    return merge

#optimized solution 
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1
        return ''.join(result)
