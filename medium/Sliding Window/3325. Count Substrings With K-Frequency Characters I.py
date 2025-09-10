class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        count = 0
        frequency = defaultdict(int)
        left = 0

        for char in s:
            frequency[char] += 1
            while frequency[char] == k:
                frequency[s[left]] -= 1
                left += 1
            count += left
        return count