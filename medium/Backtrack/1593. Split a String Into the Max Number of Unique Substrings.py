class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        return self.backtrack(s, set(), 0)

    
    def backtrack(self, s, seen, start):
        if start == len(s):
            return 0
        
        maxCount = 0
        for end in range(start+1, len(s)+1):
            substring = s[start:end]
            if substring not in seen:
                seen.add(substring)
                maxCount = max(maxCount, 1+self.backtrack(s, seen, end))
                seen.remove(substring)
        return maxCount