class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        for row in range(m):
            for col in range(n):
                if self.backtrack(board, word, 0, row, col):
                    return True
        return False

    def backtrack(self, board, word, idx, row, col):
        if idx == len(word):
            return True
        
        if not 0<=row<len(board) or not 0<=col<len(board[0]) or board[row][col] != word[idx]:
            return False
        
        board[row][col] = '.'
        ans = self.backtrack(board, word, idx+1, row+1, col) or self.backtrack(board, word, idx+1, row-1, col) or self.backtrack(board, word, idx+1, row, col+1) or self.backtrack(board, word, idx+1, row, col-1)
        board[row][col] = word[idx]