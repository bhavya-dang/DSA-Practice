def countDigitsInNumber(n):
    count = 0 # counter / accumulator
    while n > 0:
        count += 1 # increment
        n = n // 10 # floor divide to remove last digit
    return count

def countDigitsInNumber(n):
    count = 0 # counter / accumulator
    for i in str(n):
        count += 1 # increment
    return count, i

                                

if __name__ == "__main__":
    num = 123
    print("N:", num)
    digits = countDigitsInNumber(num)
    print("Number of Digits in N:", digits[0])
                                
                            