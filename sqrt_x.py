class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x
        answer = 0

        while left <= right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                answer = mid
                left = mid + 1

            else:
                right = mid - 1

        return answer


# Test
solution = Solution()

print(solution.mySqrt(4))
print(solution.mySqrt(8))
print(solution.mySqrt(25))