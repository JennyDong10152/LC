class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        self.answer = False
        self.backtrack(pattern, s, 0, {})
        return self.answer
    
    def backtrack(self, pattern, s, idx, pattern_dict):
        if idx == len(pattern):
            if not s:
                self.answer = True
            return

        current = pattern[idx]
        for i in range(len(s)):
            substring = s[:i+1]
            leftover = s[i+1:]
            if not current in pattern_dict and not substring in pattern_dict.values():
                pattern_dict[current] = substring
                self.backtrack(pattern, leftover, idx+1, pattern_dict)
                del pattern_dict[current]
            elif current in pattern_dict and pattern_dict[current] == substring:
                self.backtrack(pattern, leftover, idx+1, pattern_dict)