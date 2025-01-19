class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and self.backtrack(row, col, 0, board, word):
                    return True
        return False

    def backtrack(self, row, col, idx, board, word):
        if idx == len(word):
            return True
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or board[row][col] != word[idx]:
            return False
        
        char = board[row][col]
        board[row][col] = '.'
        if self.backtrack(row+1, col, idx+1, board, word) or self.backtrack(row-1, col, idx+1, board, word) or self.backtrack(row, col+1, idx+1, board, word) or self.backtrack(row, col-1, idx+1, board, word):
            return True
        board[row][col] = char
        return False