def ToH(n, start, temp, finish):
    if n<=0: return
    ToH(n-1,start, finish, temp)
    print(start + ' to ' + finish)
    ToH(n-1, temp, start, finish)

ToH(3, 'A', 'B', 'C')