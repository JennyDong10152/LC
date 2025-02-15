class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.reference = {"2": "abc", "3" : "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9" :"wxyz"}
        self.answers = []
        self.backtrack(digits, 0, [])
        return self.answers
    
    def backtrack(self, digits, idx, temp):
        if idx == len(digits):
            self.answers.append("".join(temp))
            return
        
        for letter in self.reference[digits[idx]]:
            temp.append(letter)
            self.backtrack(digits, idx+1, temp)
            temp.pop()