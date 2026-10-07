class Solution:
    def partition(self, s: str) -> list[list[str]]:
        self.ans = []
        self.backtrack(s, 0, [])
        return self.ans
    
    def backtrack(self, s, start, current):
        if start == len(s):
            self.ans.append(list(current))
            return
        
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if word == word[::-1]:
                current.append(word)
                self.backtrack(s, end, current)
                current.pop()