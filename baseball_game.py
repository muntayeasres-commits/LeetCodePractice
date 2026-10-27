
class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(op))

        return sum(stack)


operations = ["5", "2", "C", "D", "+"]
solution = Solution()

result = solution.calPoints(operations)
print("Operations:", operations)
print("Total score:", result)
