class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
        self.backtrack(n, 0, 0, [])
        return self.ans
<<<<<<< Updated upstream
    
    def backtrack(self, n, left, right, current):
        if left == right and right == n:
            self.ans.append(''.join(current))
=======

    def backtrack(self, n, left, right, current):
        if left == right == n:
            self.ans.append(''.join(current))
            return
>>>>>>> Stashed changes
        
        if left < n:
            current.append('(')
            self.backtrack(n, left+1, right, current)
            current.pop()
            current.append('(')
            self.backtrack(n, left+1, right, current)
            current.pop()
        
<<<<<<< Updated upstream
        if right<left:
=======
        if right < left:
>>>>>>> Stashed changes
            current.append(')')
            self.backtrack(n, left, right+1, current)
            current.pop()