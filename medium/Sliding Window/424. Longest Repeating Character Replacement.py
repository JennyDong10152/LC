class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        maxFrequency = 0
        left = 0
        frequency = defaultdict(int)

        for right, char in enumerate(s):
            frequency[char] += 1
            maxFrequency = max(maxFrequency, frequency[char])
            while (right-left+1) - maxFrequency > k:
                frequency[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength