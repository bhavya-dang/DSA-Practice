class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                return False
        return True
    
sol = Solution()
print(sol.check([1, 2, 6, 4, 5])) # False
print(sol.check([1, 2, 3, 4, 5])) # True