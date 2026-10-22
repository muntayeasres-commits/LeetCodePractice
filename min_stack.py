
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []

    def push(self, value: int) -> None:
        self.stack.append(value)

        if not self.minimums:
            self.minimums.append(value)
        else:
            self.minimums.append(min(value, self.minimums[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minimums.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimums[-1]


# Test Case 1
obj = MinStack()

obj.push(-2)
obj.push(0)
obj.push(-3)

print(obj.getMin())

obj.pop()

print(obj.top())
print(obj.getMin())
