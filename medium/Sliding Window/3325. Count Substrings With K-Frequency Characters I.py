class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        count = 0
        left = 0
        frequency = defaultdict(int)

        for right, char in enumerate(s):
            frequency[char] += 1
            while frequency[char] == k:
                frequency[s[left]] -= 1
                left += 1
            count += left
        return count