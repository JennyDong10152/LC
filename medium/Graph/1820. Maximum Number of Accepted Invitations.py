class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.matches = {} #girl : boy
            
        for boy in range(m):
            self.search(boy, set())
            
        return len(self.matches)

    def search(self, boy, visited):
        for girl in range(self.n):
            if self.grid[boy][girl] and girl not in visited:
                visited.add(girl)
                
                if girl not in self.matches or self.search(self.matches[girl], visited): 
                    self.matches[girl] = boy                        
                    return True
        return False