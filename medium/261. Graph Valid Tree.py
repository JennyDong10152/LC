class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return False
        
        parent = [i for i in range(n)]
        for u, v in edges:
            if not self.union(parent, u, v):
                return False
        return True
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x == root_y:
            return False
        parent[root_x] = root_y
        return True
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]