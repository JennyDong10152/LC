class Solution:
    def reorganizeString(self, s: str) -> str:
        frequency = defaultdict(int)
        for char in s:
            frequency[char] += 1
        sorted_chars = sorted(frequency.keys(), key = lambda x: frequency[x], reverse = True)
        if frequency[sorted_chars[0]] > (len(s) + 1) // 2:
            return ""
        
        answer = [None] * len(s)
        idx = 0
        for char in sorted_chars:
            for _ in range(frequency[char]):
                if idx >= len(s):
                    idx = 1
                answer[idx] = char
                idx += 2
        return "".join(answer)