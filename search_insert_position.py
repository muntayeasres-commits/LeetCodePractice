from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if i == target:
                return nums.index(i)
            elif i > target:
                return nums.index(i)
        else:
            return len(nums)


# Test
nums = [1, 3, 5, 6]
target = 5

solution = Solution()
result = solution.searchInsert(nums, target)

print("Index:", result)