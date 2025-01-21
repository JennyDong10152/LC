class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        self.answer = []
        self.search(0, [], s, wordDict)
        return self.answer
    
    def search(self, start, temp, s, wordDict):
        if start == len(s):
            self.answer.append(" ".join(temp))
            return
        for end in range(start+1, len(s) + 1):
            word = s[start:end]
            if word in wordDict:
                temp.append(word)
                self.search(end, temp, s, wordDict)
                temp.pop()