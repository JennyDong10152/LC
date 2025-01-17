class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.backtrack(s, 0, seen)
    
    def backtrack(self, s, start, seen):
        if start == len(s):
            return 0
        
        maxCount = 0
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if substring not in seen:
                seen.add(substring)
                maxCount = max(maxCount, 1 + self.backtrack(s, end, seen))
                seen.remove(substring)
        return maxCount