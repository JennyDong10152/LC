class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visited = defaultdict(int)
        maxLength = 0

        for right, char in enumerate(s):
            if char in visited and visited[char] >= left:
                left = visited[char] + 1
            maxLength = max(maxLength, right - left + 1)
            visited[char] = right
        return maxLength