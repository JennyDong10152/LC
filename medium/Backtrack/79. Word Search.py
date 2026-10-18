class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for row in range(m):
            for col in range(n):
                exist = self.backtrack(board, row, col, word, 0)
                if exist:
                    return True
        return False
    
    def backtrack(self, board, row, col, word, idx):
        if idx == len(word):
            return True

        if not 0<=row<len(board) or not 0<=col<len(board[0]) or board[row][col] != word[idx]:
            return False

        board[row][col] = '.'
        exist = self.backtrack(board, row+1, col, word, idx+1) or self.backtrack(board, row-1, col, word, idx+1) or self.backtrack(board, row, col+1, word, idx+1) or self.backtrack(board, row, col-1, word, idx+1)
        board[row][col] = word[idx]
        return exist