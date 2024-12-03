class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        for u, v in edges:
            self.union(parent, u, v)

        components = defaultdict(int)
        for i in range(n):
            parent_root = self.find(parent, i)
            components[parent_root] += 1
        
        total = n * (n-1) // 2
        for parent_root, size in components.items():
            total -= ((size) * (size-1) // 2)
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