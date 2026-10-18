class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        maxGold = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                gold = self.backtrack(grid, row, col, 0)
                maxGold = max(maxGold, gold)
        return maxGold
    
    def backtrack(self, grid, row, col, gold):
        if not 0<=row<len(grid) or not 0<=col<len(grid[0]) or not grid[row][col]:
            return gold
        
        gold += grid[row][col]
        current = grid[row][col]
        grid[row][col] = 0
        optimal = max(self.backtrack(grid, row+1, col, gold), self.backtrack(grid, row-1, col, gold), self.backtrack(grid, row, col+1, gold), self.backtrack(grid, row, col-1, gold))
        grid[row][col] = current
        return optimal
        