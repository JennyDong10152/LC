class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        maxLength = left = maxFrequency = 0

        for right, char in enumerate(s):
            frequency[char] += 1
            maxFrequency = max(maxFrequency, frequency[char])
            if right-left+1 - maxFrequency > k:
                frequency[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength