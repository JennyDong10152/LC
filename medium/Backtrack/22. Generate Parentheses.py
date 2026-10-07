class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        self.ans = []
        self.backtrack(n, 0, 0, [])
        return self.ans
    
    def backtrack(self, n, left, right, current):
        if left == right and right == n:
            self.ans.append(''.join(current))
        
        if left < n:
            current.append('(')
            self.backtrack(n, left+1, right, current)
            current.pop()
        
        if right<left:
            current.append(')')
            self.backtrack(n, left, right+1, current)
            current.pop()