class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        visited = defaultdict(int)
        maxLength = 0

        for idx, char in enumerate(s):
            if char in visited and visited[char] >= left:
                left = visited[char]+1
            visited[char] = idx
            maxLength = max(maxLength, idx-left+1)
        return maxLength