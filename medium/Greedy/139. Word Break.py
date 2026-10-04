class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for idx in range(len(s) + 1):
            for word in wordDict:
                start = idx - len(word)
                if start >=0 and s[start : idx] == word and dp[start]:
                    dp[idx] = True
        return dp[len(s)]