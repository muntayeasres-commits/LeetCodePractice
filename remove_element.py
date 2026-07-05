from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Test
nums = [3, 2, 2, 3]
val = 3

solution = Solution()
k = solution.removeElement(nums, val)

print("k =", k)
print("Valid elements:", nums[:k])
print("Full array:", nums)