def isArmstrong(n:int) -> int:
    temp = n
    sum = 0
    while n > 0:
        lastDigit = n % 10
        sum += lastDigit ** 3
        n = n // 10
    return sum == temp

print(isArmstrong(371))