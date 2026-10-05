class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        disjoint = n
        parent = [i for i in range(n)]

        for idx, cities in enumerate(isConnected):
            for city in range(len(cities)):
                if isConnected[idx][city] == 1 and self.union(parent, idx, city):
                    disjoint -= 1
        return disjoint
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]