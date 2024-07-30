def allDivisors(n:int) -> list: 
    allDivisorsList = []
    for i in range (1, n+1, 1):
        allDivisorsList.append(n/i)
print(allDivisors(36))  