class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        maxLength = 0
        left = 0 

        for right, char in enumerate(s):
            frequency[char] += 1
            while len(frequency) > k:
                frequency[s[left]] -= 1
                if not frequency[s[left]]:
                    del frequency[s[left]]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength