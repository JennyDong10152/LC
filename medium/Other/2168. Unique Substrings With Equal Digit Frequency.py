class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        unique = set()
        for i in range(n):
            frequency = defaultdict(int)
            temp = ''
            for j in range(i, n):
                frequency[s[j]] += 1
                temp += s[j]
                if len(set(frequency.values())) == 1:
                    unique.add(temp)
        return len(unique)