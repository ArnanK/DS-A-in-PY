def bad_fib(n):
    if n<=1: return 1
    else:
        return bad_fib(n-2) + bad_fib(n-1)

def good_fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a, b) = good_fibonacci(n-1)
        return (a+b, a)

#dynamic fib
def fibbonacci(n):
    table = [-1 for _ in range(n+1)]
    table[0] = 0
    table[1] = 1
    dynamic_fib(n,table)
    return table[n]

def dynamic_fib(n, table):
    if table[n] != -1: return table[n]
    dynamic_fib(n-1, table)
    dynamic_fib(n-2, table)
    table[n] = table[n-1] + table[n-2]
    return table[n] 


print(fibbonacci(8))