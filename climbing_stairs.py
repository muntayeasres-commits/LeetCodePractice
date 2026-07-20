class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [1, 2]

        if n <= 2:
            return n

        for i in range(3, n + 1):
            ways.append(ways[-1] + ways[-2])

        return ways[-1]


# Test
solution = Solution()

print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(5))