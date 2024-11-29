class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        parent = [i for i in range(n)]
        groups = n

        for time, x, y in logs:
            if self.union(parent, x, y):
                groups -= 1
            if groups == 1:
                return time
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
    #reviewed