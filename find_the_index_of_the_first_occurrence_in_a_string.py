class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack or not needle:
            return -1
        else:
            return haystack.find(needle)


# Test
haystack = "sadbutsad"
needle = "sad"

solution = Solution()
result = solution.strStr(haystack, needle)

print("Index:", result)