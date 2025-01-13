class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = dict()
        maxLength = 0
        left = 0

        for right, char in enumerate(s):
            if char in visited and left <= visited[char]:
                left = visited[char] + 1
            visited[char] = right
            maxLength = max(maxLength, right - left + 1)
        return maxLength