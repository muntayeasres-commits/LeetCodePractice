from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        strr = ""

        for i in digits:
            strr += str(i)

        new_num = int(strr) + 1

        x = [int(j) for j in str(new_num)]

        return x


# Test
solution = Solution()

print(solution.plusOne([1, 2, 3]))
print(solution.plusOne([4, 3, 2, 1]))
print(solution.plusOne([9]))