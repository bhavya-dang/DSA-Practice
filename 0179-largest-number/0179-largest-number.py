class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1

        return str(int("".join(sorted([str(num) for num in nums], key=cmp_to_key(compare)))))

        