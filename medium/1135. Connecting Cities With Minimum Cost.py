class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        connections = sorted(connections, key = lambda x : x[2])
        minCost = 0
        parent = [i for i in range(n+1)]
        disjointed = n

        for u, v, cost in connections:
            if self.union(parent, u, v):
                minCost += cost
                disjointed -= 1
                if disjointed == 1:
                    return minCost
        return -1
    
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