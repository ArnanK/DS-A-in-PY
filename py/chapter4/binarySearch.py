data = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]

#Recursive Binary Search O(log(n))
def binary_search(data, target, low, high):
    if low>high: return False
    else:
        mid = low + (high-low)//2
        if(data[mid] == target): return True
        elif(data[mid] < target): return binary_search(data, target, mid+1, high)
        else: return binary_search(data, target, low, mid-1)
#F(n)=F(n/2) +1
#F(n/2^k) + k



print(binary_search(data, 4,0,len(data)-1))
