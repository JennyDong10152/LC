class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
<<<<<<< Updated upstream
        n = len(s)
        maxLength = left = 0
        unique = defaultdict(int)

        for right in range(n):
            unique[s[right]] += 1
            while len(unique) > k:
                unique[s[left]] -= 1
                if not unique[s[left]]:
                    del unique[s[left]]
=======
        frequency = defaultdict(int)
        maxLength = 0
        left = 0

        for right, char in enumerate(s):
            frequency[char] += 1
            if len(frequency) > k:
                frequency[s[left]] -= 1
                if not frequency[s[left]]:
                    del frequency[s[left]]
>>>>>>> Stashed changes
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength
