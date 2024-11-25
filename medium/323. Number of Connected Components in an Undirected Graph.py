class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        cnt = 0

        for u, v in edges:
            self.union(parent, u, v)

        cnt = set()
        for i in parent:
            cnt.add(self.find(parent, i))
        return len(cnt)
    
    def union(self, parent, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)
        if root_u != root_v:
            parent[root_u] = root_v
        return False
    
    def find(self, parent, curr):
        if parent[curr] != curr:
            parent[curr] = self.find(parent, parent[curr])
        return parent[curr]