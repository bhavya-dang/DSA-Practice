import math
def isPrime(n:int) -> bool:
    # method 1, time complexity is O(n)
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    

    # method 2, time complexity is O(sqrt(n))
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            counter += 1

            if n//i != i:
                counter += 1


    if counter == 2:
        return True
    return False

print(isPrime(2))