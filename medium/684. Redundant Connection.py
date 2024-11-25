class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        cycle = []
        for u, v in edges:
            if self.union(parent, u, v):
                cycle = [u, v]
        return cycle
    
    def union(self, parent, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)
        if root_u != root_v:
            parent[root_u] = root_v
            return False
        return True
    
    def find(self, parent, curr):
        if curr != parent[curr]:
            parent[curr] = self.find(parent, parent[curr])
        return parent[curr]