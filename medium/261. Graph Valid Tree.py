class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1: 
            return False
        parent = [i for i in range(n)]
        for u, v in edges:
            if not self.union(parent, u, v):
                return False
        return True

    def union(self, parent, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)
        if root_u == root_v:
            return False
        parent[root_u] = root_v
        return True

    def find(self, parent, curr):
        if parent[curr] != curr:
            parent[curr] = self.find(parent, parent[curr])
        return parent[curr]