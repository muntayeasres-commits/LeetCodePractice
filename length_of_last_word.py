from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        text = s.split()
        sub_text = text[-1]
        return len(sub_text)


# Test
solution = Solution()

print(solution.lengthOfLastWord("Hello World"))
print(solution.lengthOfLastWord("   fly me   to   the moon  "))
print(solution.lengthOfLastWord("luffy is still joyboy"))