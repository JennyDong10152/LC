class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(word, 0, row, col, board):
                    return True
        return False
    
    def backtrack(self, word, idx, row, col, board):
        if idx == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[idx]:
            return False
        
        board[row][col] = '.'
        answer = self.backtrack(word, idx+1, row+1, col, board) or self.backtrack(word, idx+1, row-1, col, board) or self.backtrack(word, idx+1, row, col+1, board) or self.backtrack(word, idx+1, row, col-1, board)
        board[row][col] = word[idx]
        return answer