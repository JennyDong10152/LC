class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        parent = {}
        value = {}

        for (x, y), val in zip(equations, values):
            root_x, val_x = self.find(parent, value, x)
            root_y, val_y = self.find(parent, value, y)

            if root_x == root_y:
                if abs((val_x / val_y) - val) > 1e-5:
                    return True
            else:
                self.union(parent, value, x, y, val)
        
        return False
    
    def union(self, parent, value, x, y, val):
        root_x, val_x = self.find(parent, value, x)
        root_y, val_y = self.find(parent, value, y)
        parent[root_x] = root_y
        value[root_x] = val * val_y / val_x
    
    def find(self, parent, value, x):
        if x not in parent:
            parent[x] = x
            value[x] = 1.0
        if parent[x] != x:
            parent[x], ratio = self.find(parent, value, parent[x])
            value[x] *= ratio 
        return parent[x], value[x]