class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key = lambda x : x[0])
        parent = [i for i in range(n)]
        disjoint = n

        for time, x, y in logs:
            connected = self.union(parent, x, y)
            if connected:
                disjoint -= 1
                if disjoint == 1:
                    return time
        return -1
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]