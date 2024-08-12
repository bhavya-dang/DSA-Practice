"""Calculates the sum of all numbers from 1 to n"""
def recursive_sum(n: int) -> int:
    if n < 1:
        return 0
    else:
        print(n, end=" + " if n > 1 else "")
        return n + recursive_sum(n-1)

print("Numbers to add: ", end="")
result = recursive_sum(10)
print(" = ", result)