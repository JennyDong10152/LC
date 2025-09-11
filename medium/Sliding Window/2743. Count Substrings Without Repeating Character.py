class Solution:
    def numberOfSpecialSubstrings(self, s: str) -> int:
        left = 0
        count = 0
        frequency = defaultdict(int)

        for right, char in enumerate(s):
            if char in frequency and left <= frequency[char]:
                left = frequency[char] + 1
            frequency[char] = right
            count += right - left + 1
        return count