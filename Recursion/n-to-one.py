def recFn(n:int):
    if (n < 1): return
    print(n, end=' ')
    recFn(n-1)

recFn(10)

# this gives the same output as 
# for i in range (10, 0, -1):
#     print(i, end=' ')