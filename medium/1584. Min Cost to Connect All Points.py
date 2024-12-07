class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = self.distance(points)
        cost.sort(key = lambda x : x[0])
        n = len(points)
        parent = [i for i in range(n)]
        minCost = 0

        for c, x, y in cost:
            if self.union(parent, x, y):
                minCost += c
        return minCost
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
            return True
        return False
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def distance(self, points):
        cost = []
        n = len(points)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dis = abs(x2-x1) + abs(y2-y1)
                cost.append([dis, i, j])
        return cost