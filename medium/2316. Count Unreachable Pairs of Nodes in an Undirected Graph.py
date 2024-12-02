class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        for u, v in edges:
            self.union(parent, u, v)
        
        component = defaultdict(int)
        for i in range(n):
            root = self.find(parent, i)
            component[root] += 1
        
        total = n * (n - 1) // 2
        
        for size in component.values():
            total -= size * (size - 1) // 2
        return total
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
        
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]