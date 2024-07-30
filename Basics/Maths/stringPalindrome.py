def isStringPalindrome(s: str) -> bool:
    reversedStr = s[::-1]  
    return s == reversedStr

print(isStringPalindrome("hello"))  # False
print(isStringPalindrome("madam"))  # True