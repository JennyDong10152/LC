class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
<<<<<<< Updated upstream
        visited = dict()
        left = 0
        maxLength = 0

        for right, char in enumerate(s):
            if char in visited and left <= visited[char]:
                left = visited[char] + 1
            maxLength = max(maxLength, right - left + 1)
            visited[char] = right
=======
        maxLength = 0
        frequency = defaultdict()
        left = 0

        for right, char in enumerate(s):
            if char in frequency and left <= frequency[char]:
                left = frequency[char] + 1
            frequency[char] = right
            maxLength = max(maxLength, right - left + 1)
>>>>>>> Stashed changes
        return maxLength