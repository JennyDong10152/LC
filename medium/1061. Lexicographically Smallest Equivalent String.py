class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {c : c for c in s1}
        parent.update({c : c for c in s2})

        for c, d in zip(s1, s2):
            self.union(parent, c, d)
        
        ans = ""
        for c in baseStr:
            ans += (self.find(parent, c))
        return ans
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x < root_y:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if x not in parent:
            return x
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
