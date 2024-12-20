class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n+1)]
        disjoint = n

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    connect = self.union(parent, i, j)
                    if connect:
                        disjoint -= 1
        return disjoint
    
    def union(self, parent, i, j):
        root_i = self.find(parent, i)
        root_j = self.find(parent, j)
        if root_i != root_j:
            parent[root_j] = root_i
            return True
        return False
    
    def find(self, parent, i):
        if i != parent[i]:
            parent[i] = self.find(parent, parent[i])
        return parent[i]