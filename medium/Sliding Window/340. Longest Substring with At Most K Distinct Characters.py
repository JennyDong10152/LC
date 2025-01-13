class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        maxLength = left = 0
        unique = defaultdict(int)

        for right in range(n):
            unique[s[right]] += 1
            while len(unique) > k:
                unique[s[left]] -= 1
                if not unique[s[left]]:
                    del unique[s[left]]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength