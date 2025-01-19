class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        self.answer = False
        self.backtrack(s, 0, pattern, {})
        return self.answer
    
    def backtrack(self, string, idx, pattern, pattern_dict):
        if idx == len(pattern):
            if not string:
                self.answer = True
            return
        
        current = pattern[idx]
        for i in range(len(string)):
            substring = string[:i+1]
            leftover = string[i+1:]
            if current not in pattern_dict and substring not in pattern_dict.values():
                pattern_dict[current] = substring
                self.backtrack(leftover, idx+1, pattern, pattern_dict)
                del pattern_dict[current]
            elif current in pattern_dict and pattern_dict[current] == substring:
                self.backtrack(leftover, idx+1, pattern, pattern_dict)
        