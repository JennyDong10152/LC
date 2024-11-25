class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n+1)]
        degree = {}  
        doubleParent1 = doubleParent2 = None  

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

    def find(self, parent, curr):
        if parent[curr] != curr:
            parent[curr] = self.find(parent, parent[curr])
        return parent[curr]

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x == root_y:
            #cycle
            return False 
        parent[root_y] = root_x
        return True