class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
<<<<<<< Updated upstream
        n = len(s)
        maxLength = 0
        maxFrequency = 0
        left = 0
        count = defaultdict(int)

        for right in range(n):
            count[s[right]] += 1
            maxFrequency = max(maxFrequency, count[s[right]])
            if (right - left + 1) - maxFrequency > k:
                count[s[left]] -= 1
=======
        frequency = defaultdict(int)
        left = 0
        maxLength = maxFrequency = 0

        for right, char in enumerate(s):
            frequency[char] += 1
            maxFrequency = max(maxFrequency, frequency[char]) 
            if (right-left+1) - maxFrequency > k:
                frequency[s[left]] -= 1
>>>>>>> Stashed changes
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength