class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1 for i in range(n)]
        edge = [0 for i in range(n)]
        ans = 0
        for u,v in edges:
            self.union(parent, rank, edge, u, v)
        
        for i in range(n):
            if i == self.find(parent, i):
                if edge[i] == rank[i]*(rank[i]-1) // 2:
                    ans += 1
        return ans
    
    def union(self, parent, rank, edge, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                root_x, root_y = root_y, root_x
            parent[root_y] = root_x
            edge[root_x] += edge[root_y]
            rank[root_x] += rank[root_y] 
        edge[root_x] += 1
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
