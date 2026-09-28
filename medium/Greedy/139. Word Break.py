class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for idx in range(len(s) + 1):
            for word in wordDict:
                n = len(word)
                if idx >= n and s[idx - n : idx] == word and dp[idx - n]:
                    dp[idx] = True
        return dp[len(s)]