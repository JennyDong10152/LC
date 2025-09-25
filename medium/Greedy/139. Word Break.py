class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordDict = set(wordDict)

        for idx in range(1, len(s) + 1):
            for word in wordDict:
                start = idx - len(word)
                if start >= 0 and s[start : idx] == word and dp[start]:
                    dp[idx] = True
        return dp[len(s)]