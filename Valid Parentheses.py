
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for ch in s:
            # if opening bracket, push to stack
            if ch in mapping.values():
                stack.append(ch)
            else:
                # if stack empty or top doesn't match
                if not stack or stack.pop() != mapping[ch]:
                    return False

        # stack must be empty at the end
        return not stack