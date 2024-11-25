class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        parent = [i for i in range(m)] 

        for i in range(m):
            for j in range(m):
                if isConnected[i][j] == 1:
                    self.union(parent, i, j)
        disjoint = set()
        for i in range(m):
            disjoint.add(self.find(parent, i))

        return len(disjoint)

    def union(self, parent, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)
        if root_u != root_v:
            parent[root_u] = root_v

    def find(self, parent, curr):
        if parent[curr] != curr:
            parent[curr] = self.find(parent, parent[curr])
        return parent[curr]
