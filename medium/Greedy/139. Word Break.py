class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[0] = True
        wordDict = set(wordDict)

        for end in range(1, len(s)+1):
            for word in wordDict:
                start = end - len(word)
                if start >= 0 and s[start : end] == word and dp[start]:
                    dp[end] = True
        return dp[len(s)]