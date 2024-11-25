class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        parent = [i for i in range(n)]
        for u, v in edges:
            self.union(parent, u, v)
        return self.find(parent, source) == self.find(parent, destination)

    def union(self, parent, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)
        if root_u != root_v:
            parent[root_u] = root_v

    def find(self, parent, curr):
        if parent[curr] != curr:
            parent[curr] = self.find(parent, parent[curr])
        return parent[curr]