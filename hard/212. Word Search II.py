class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        answer = []
        for word in words:
            if self.exist(word, board):
                answer.append(word)
        return answer
    
    def exist(self, word, board):
        if len(word) > len(board) * len(board[0]):
            return False
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(row, col, 0, board, word):
                    return True
        return False
    
    def backtrack(self, row, col, idx, board, word):
        if idx == len(word):
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[idx]:
            return False
        char = board[row][col]
        board[row][col] = '.'
        exists = self.backtrack(row+1, col, idx+1, board, word) or self.backtrack(row-1, col, idx+1, board, word) or self.backtrack(row, col+1, idx+1, board, word) or self.backtrack(row, col-1, idx+1, board, word)
        board[row][col] = char
        return exists