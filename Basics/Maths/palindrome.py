def isPalindrome(n:int) -> bool:
    temp = n
    acc = 0
    while n > 0:
        lastDigit = n % 10 # gets last digit from remainder
        acc = acc * 10 + lastDigit # multiply with 10 to move its pos in every iteration to the left 
        n = n // 10 # shave off last digit from input num
    print("temp: ", temp, "n: ", acc)
    
    # remove leading zeroes from acc
    acc = int(str(acc).lstrip('0'))
    
    if (temp == acc):
        return True
    else:
        return False

print(isPalindrome(333000))