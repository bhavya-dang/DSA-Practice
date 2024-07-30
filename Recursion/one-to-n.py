def recFn(i:int, n:int):
    if (i > n): return
    print(i, end=' ')
    recFn(i+1, n)

recFn(3, 10)

# this gives the same output as for i in range (3, 11)