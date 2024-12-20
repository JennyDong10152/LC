class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        parent = {(i, j) : (i, j) for i in range(m) for j in range(n) if board[i][j] == "O"}
        direction = [(-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    for di, dj in direction:
                        new_i = di + i
                        new_j = dj + j
                        if 0 <= new_i < m and 0 <= new_j < n and board[new_i][new_j] == 'O':
                            self.union(parent, (i, j), (new_i, new_j))
        graph = defaultdict(list)
        boundary = set()
        for x, y in parent:
            root = self.find(parent, (x, y))
            if not x or not y or x==m-1 or y==n-1:
                boundary.add(root)
            graph[root].append((x, y))
        
        for x, y in parent:
            root = self.find(parent, (x,y))
            if not root in boundary:
                board[x][y] = 'X'
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]