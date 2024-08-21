class Solution:
    def removeDuplicates(self, nums: list[int]):
        if not nums:
            return 0

        # Initialize the pointer for the position of the unique element
        i = 0

        # Traverse the array with j starting from the second element
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        # The length of the array with unique elements is i + 1
        return i + 1