class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.n = n
        answer = []
        visited_cols = set()
        visited_diagnols = set()
        visited_antidiagnols = set()
        self.backtrack(0, visited_cols, visited_diagnols, visited_antidiagnols, answer)
        return answer
    
    def backtrack(self, row, visited_cols, visited_diagnols, visited_antidiagnols, answer):
        if row == self.n:
            answer.append(["".join(row) for row in self.board])
            return 
        
        for col in range(self.n):
            diagnolDiff = row - col
            diagnolSum = row + col
            if (col in visited_cols) or (diagnolDiff in visited_diagnols) or (diagnolSum in visited_antidiagnols):
                continue
            visited_cols.add(col)
            visited_diagnols.add(diagnolDiff)
            visited_antidiagnols.add(diagnolSum)
            self.board[row][col] = 'Q'

            self.backtrack(row+1, visited_cols, visited_diagnols, visited_antidiagnols, answer)

            visited_cols.remove(col)
            visited_diagnols.remove(diagnolDiff)
            visited_antidiagnols.remove(diagnolSum)
            self.board[row][col] = '.'