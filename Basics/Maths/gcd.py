def gcd(x:int, y:int) -> int:
    gcd = 0
    for i in range(1, max(x,y)): # increasing range so that last iteration will be checking for greatest value
        if (x % i == 0 and y % i == 0): # check if curr number divides both of the numbers
            gcd = i
    return gcd

print(gcd(9, 12))

# WC Time Complexity: O(min(x,y))