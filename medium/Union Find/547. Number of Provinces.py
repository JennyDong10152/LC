class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        disjoint = n
        parent = [i for i in range(n)]

        for city in range(n):
            for neighbor in range(n):
                if isConnected[city][neighbor]==1 and self.union(parent, city, neighbor):
                    disjoint-=1
        return disjoint
    
    def union(self, parent, x, y):
        root_x = self.find(parent,x)
        root_y = self.find(parent,y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False

    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]