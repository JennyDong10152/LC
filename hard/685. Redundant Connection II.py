class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        doubleParent1 = doubleParent2 = None
        degree = defaultdict()
        parent = [i for i in range(n+1)]

        for u, v in edges:
            if v in degree:
                doubleParent1 = [degree[v], v]
                doubleParent2 = [u, v]
            else:
                degree[v] = u

        for u, v in edges: 
            if [u, v] == doubleParent2:
                continue
            if not self.union(parent, u, v):
                if doubleParent1:
                    return doubleParent1
                return [u, v]
        return doubleParent2
    
    def union(self, parent, u, v):
        root_u = self.find(parent, u)
        root_v = self.find(parent, v)
        if root_u == root_v:
            return False
        parent[root_u] = root_v
        return True

    def find(self, parent, curr):
        if curr != parent[curr]:
            parent[curr] = self.find(parent, parent[curr])
        return parent[curr] 