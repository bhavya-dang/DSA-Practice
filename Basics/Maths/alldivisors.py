def allDivisors(n:int) -> list: 
    allDivisorsList = []
    for i in range (1, n+1):
        if n % i == 0:
            allDivisorsList.append(i)
    return allDivisorsList
print(allDivisors(36))  