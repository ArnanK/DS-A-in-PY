def insertion_sort(A):
    """
    The function `insertion_sort` implements the insertion sort algorithm to sort a given list `A` in
    ascending order.
    
    :param A: The parameter A is a list of elements that we want to sort using the insertion sort
    algorithm
    """
    for k in range(1,len(A)):
        curr = A[k]
        j=k
        while j>0 and A[j-1] > curr:
            A[j] = A[j-1]
            j-=1
        A[j]=curr