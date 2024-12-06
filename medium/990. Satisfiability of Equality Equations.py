class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {c[0] : c[0] for c in equations}
        parent.update({c[3] : c[3] for c in equations})

        for equation in equations:
            if equation[1:3] == "==":
                self.union(parent, equation[0], equation[3])
        
        for equation in equations:
            if equation[1:3] == "!=":
                root_x = self.find(parent, equation[0])
                root_y = self.find(parent, equation[3])
                if root_x == root_y:
                    return False
                
        return True
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]