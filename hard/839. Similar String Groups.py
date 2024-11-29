class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = [i for i in range(n)]
        
        for i in range(n):
            for j in range(i+1, n):
                root_i = self.find(parent, i)
                root_j = self.find(parent, j)
                if root_i != root_j and self.areSimilar(strs[i], strs[j]):
                    self.union(parent, i, j)
        
        disjoint = set()
        for i in parent:
            disjoint.add(self.find(parent, i))
        return len(disjoint)

    def areSimilar(self, x, y):
        diff = 0
        for c, d in zip(x, y):
            if c != d:
                diff += 1
        return diff <= 2

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y