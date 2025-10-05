class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(row, col, word, 0, board):
                    return True
        return False
    
    def backtrack(self, row, col, word, idx, board):
        if idx == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[idx]:
            return False
        
        board[row][col] = '.'
        answer = self.backtrack(row+1, col, word, idx+1, board) or self.backtrack(row-1, col, word, idx+1, board) or self.backtrack(row, col+1, word, idx+1, board) or self.backtrack(row, col-1, word, idx+1, board)
        board[row][col] = word[idx]
        return answer