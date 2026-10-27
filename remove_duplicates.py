
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)

        return "".join(stack)


# Test your solution
solution = Solution()

print(solution.removeDuplicates("abbaca"))  # ca
print(solution.removeDuplicates("azxxzy"))  # ay
print(solution.removeDuplicates("aaaa"))    # ""
print(solution.removeDuplicates("abc"))     # abc
