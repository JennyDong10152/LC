class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        maxFrequency = 0
        left = 0
        count = defaultdict(int)

        for right, char in enumerate(s):
            count[char] += 1
            maxFrequency = max(maxFrequency, count[char])
            if (right - left + 1) - maxFrequency > k:
                count[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength