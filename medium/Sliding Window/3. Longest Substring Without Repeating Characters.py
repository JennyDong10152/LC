class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        frequency = defaultdict(int)

        for right, char in enumerate(s):
            if char in frequency and left <= frequency[char]:
                left = frequency[char] + 1
            frequency[char] = right
            maxLength = max(maxLength, right - left + 1)
        return maxLength