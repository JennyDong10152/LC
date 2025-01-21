class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        answer = left = 0
        record = defaultdict(int)
        for char in s:
            record[char] += 1
            while record[char] == k:
                record[s[left]] -= 1
                left += 1
            answer += left
        return answer