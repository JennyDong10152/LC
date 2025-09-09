class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        frequency = dict()

        for idx, char in enumerate(s):
            if char in frequency and left <= frequency[char]:
                left = frequency[char] + 1
            maxLength = max(maxLength, idx-left+1)
            frequency[char] = idx
        return maxLength