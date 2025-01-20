class Solution:
    def minCut(self, s: str) -> int:
        return self.find(s, 0,len(s))

    def find(self, s, start, end):
        if s[start:end] == s[start:end][::-1]:
            return 0

        answer = float('inf')

        for idx in range(start+1, end):
            if s[start:idx]==s[start:idx][::-1]:
                answer = min(answer, self.find(s, start,idx) + 1 + self.find(s, idx,end))
        return answer