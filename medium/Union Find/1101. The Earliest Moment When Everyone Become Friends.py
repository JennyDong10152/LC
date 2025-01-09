class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort()
        stranger = n
        parent = [i for i in range(n)]

        for time, friend1, friend2 in logs:
            if self.union(parent, friend1, friend2):
                stranger -= 1
            if stranger == 1:
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
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]