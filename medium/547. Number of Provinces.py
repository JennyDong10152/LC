class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        m = len(isConnected)
        parent = [i for i in range(m)]

        disjoint = m
        for i in range(m):
            for j in range(m):
                if isConnected[i][j]:
                    connected = self.union(parent, i, j)
                    if connected:
                        disjoint -= 1
        # for i in range(m):
        #     disjoint.add(self.find(parent, i))
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