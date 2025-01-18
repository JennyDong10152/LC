class Solution:
    def totalNQueens(self, n: int) -> int:
        self.count = 0
        self.n = n
        columns = set()
        diagnols = set()
        antidiagnols = set()
        board = [['.' for _ in range(n)] for _ in range(n)]
        self.create(0, board, columns, diagnols, antidiagnols)
        return self.count
    
    def create(self, row, board, columns, diagnols, antidiagnols):
        if row == self.n:
            self.count += 1
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

            self.create(row+1, board, columns, diagnols, antidiagnols)

            diagnols.remove(diagnol)
            antidiagnols.remove(antidiagnol)
            columns.remove(col)
            board[row][col] = '.'