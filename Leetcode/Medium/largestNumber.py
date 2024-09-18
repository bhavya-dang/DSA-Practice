from functools import cmp_to_key
def largestNumber(nums: list[int]) -> str:
    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1

    return str(int("".join(sorted([str(num) for num in nums], key=cmp_to_key(compare)))))

numbers = [3,30,34,5,9]
print(largestNumber(numbers)) 