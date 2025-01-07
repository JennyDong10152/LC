class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        visited = dict()
        left = 0

        for right, char in enumerate(s):
            if char in visited and visited[char] >= left:
                left = visited[char] + 1
            else:
                maxLength = max(maxLength, right-left+1)
            visited[char] = right
        return maxLength
