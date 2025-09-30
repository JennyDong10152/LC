class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.answer = []
        self.backtrack(n, 0, 0, [])
        return self.answer
    
    def backtrack(self, n, left, right, temp):
        if n == left and n == right:
            self.answer.append("".join(temp))
            return
        
        if left < n:
            temp.append('(')
            self.backtrack(n, left+1, right, temp)
            temp.pop()
        
        if right < left:
            temp.append(')')
            self.backtrack(n, left, right+1, temp)
            temp.pop()