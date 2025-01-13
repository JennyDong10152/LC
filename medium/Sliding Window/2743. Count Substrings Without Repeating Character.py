class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        count = 0
        left = 0
        frequency = defaultdict(int)

        for right in range(len(s)):
            frequency[s[right]] += 1
            while frequency[s[right]] > 1:
                frequency[s[left]] -= 1
                left += 1
            count += right - left + 1
        return count