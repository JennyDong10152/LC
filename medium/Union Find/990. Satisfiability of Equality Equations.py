class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        parent = {c[0] : c[0] for c in equations}
        parent.update({c[3] : c[3] for c in equations})

        for equation in equations:
            if equation[1:3] == '==':
                self.union(parent, equation[0], equation[3])

        for equation in equations:
            if equation[1:3] == '!=':
                root_first = self.find(parent, equation[0])
                root_second = self.find(parent, equation[3])
                if root_first == root_second:
                    return False
        return True
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]