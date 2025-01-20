class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxGold = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                gold = self.get(row, col, 0, grid)
                maxGold = max(maxGold, gold)
        return maxGold
    
    def get(self, row, col, gold, grid):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or not grid[row][col]:
            return gold
        current = grid[row][col]
        grid[row][col] = 0
        gold += current
        more = max(self.get(row+1, col, gold, grid), self.get(row-1, col, gold, grid), self.get(row, col+1, gold, grid), self.get(row, col-1, gold, grid))
        grid[row][col] = current
        return more