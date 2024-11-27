class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        disjoint = n

        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    connect = self.union(parent, i, j)
                    if connect:
                        disjoint -= 1
        return disjoint
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]