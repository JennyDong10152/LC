class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diagnols, antidiagnols, columns = set(), set(), set()
        self.n = n
        self.answers = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.solve(0, diagnols, antidiagnols, columns, board)
        return self.answers
    
    def solve(self, row, diagnols, antidiagnols, columns, board):
        if row == self.n:
            self.answers.append([''.join(row) for row in board])
            return 
        
        for col in range(self.n):
            diagnol = row - col
            antidiagnol = row + col
            if (col in columns) or (diagnol in diagnols) or (antidiagnol in antidiagnols):
                continue
            diagnols.add(diagnol)
            antidiagnols.add(antidiagnol)
            columns.add(col)
            board[row][col] = 'Q'

            self.solve(row+1, diagnols, antidiagnols, columns, board)

            diagnols.remove(diagnol)
            antidiagnols.remove(antidiagnol)
            columns.remove(col)
            board[row][col] = '.'