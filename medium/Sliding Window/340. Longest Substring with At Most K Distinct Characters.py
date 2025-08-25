class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        maxLength = left = 0
        n = len(s)
        unique = defaultdict(int)

        for right, char in enumerate(s):
            unique[char] += 1
            while len(unique) > k:
                unique[s[left]] -= 1
                if not unique[s[left]]:
                    del unique[s[left]]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength
