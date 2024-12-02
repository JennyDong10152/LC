class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = [i for i in range(n)]
        
        for i in range(n):
            for j in range(i+1, n):        
                if self.areSimilar(strs[i], strs[j]):
                    self.union(parent, i, j)

        disjoint = set()
        for i in range(n):
            disjoint.add(self.find(parent, i))
        return len(disjoint)
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
    
    def areSimilar(self, x, y):
        dif = 0
        for c, d in zip(x, y):
            if c!= d:
                dif += 1
        return dif <= 2