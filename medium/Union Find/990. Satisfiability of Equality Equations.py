class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:
        parent = {c[0]:c[0] for c in equations}
        parent.update({c[-1]:c[-1] for c in equations})
        
        for equation in equations:
            first = equation[0]
            second = equation[-1]
            if equation[1:3] == '==':
                self.union(parent, first, second)

        for equation in equations:
            first_root = self.find(parent, equation[0])
            second_root = self.find(parent, equation[-1])
            if equation[1:3] == '!=' and first_root == second_root:
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