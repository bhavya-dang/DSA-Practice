def recFn(n:int) -> int:
    if (n < 1): return 0
    print(n, end=' ')
    recFn(n-1)

recFn(100)

# this gives the same output as 
# for i in range (10, 0, -1):
#     print(i, end=' ')