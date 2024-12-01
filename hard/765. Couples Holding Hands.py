class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row) // 2  # Number of couples
        parent = [i for i in range(n)]
        
        for i in range(0, len(row), 2):
            self.union(parent, row[i] // 2, row[i + 1] // 2)
        
        connected = set()
        for i in range(n):
            connected.add(self.find(parent, i))
        return n - len(connected)
        
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
        
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]