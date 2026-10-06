class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        self.ref = {'1': '', '2':'abc', '3': 'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz', '0':''}
        self.ans = []
        self.backtrack(digits, 0, [])
        return self.ans
    
    def backtrack(self, digits, idx, current):
        if idx == len(digits):
            self.ans.append(''.join(current))
            return
        for char in self.ref[digits[idx]]:
            current.append(char)
            self.backtrack(digits, idx+1, current)
            current.pop()
