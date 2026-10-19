class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        parent = {(i,j):(i,j) for i in range(m) for j in range(n) if board[i][j] == 'O'}
        direction = [(0,1), (1,0),(0,-1),(-1,0)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    for di, dj in direction:
                        new_i, new_j = i+di, j+dj
                        if 0<=new_i<m and 0<=new_j<n and board[new_i][new_j]=='O':
                            self.union(parent, (i,j), (new_i, new_j))
        
        boundaries = set()
        for (i, j) in parent:
            root = self.find(parent, (i,j))
            if i==0 or i==m-1 or j==0 or j==n-1:
                boundaries.add(root)
        
        for (i, j) in parent:
            root = self.find(parent, (i,j))
            if root not in boundaries:
                board[i][j] = 'X'

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]