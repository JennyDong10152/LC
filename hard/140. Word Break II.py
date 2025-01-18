class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        results = []
        self.backtrack(s, wordSet, [], results, 0)
        return results
    
    def backtrack(self, s, wordSet, current, results, start):
        if start == len(s):
            results.append(" ".join(current))
            return 
        
        for end in range(start+1, len(s)+1):
            word = s[start:end]
            if word in wordSet:
                current.append(word)
                self.backtrack(s, wordSet, current, results, end)
                current.pop()