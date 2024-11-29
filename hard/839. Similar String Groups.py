class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n = len(strs)
        parent = [i for i in range(n)]
        self.rank = [1 for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                root_i = self.find(parent, i)
                root_j = self.find(parent, j)
                if root_i != root_j and self.are_similar(strs[i], strs[j]):
                    self.union(parent, i, j)

        disjoint = set()
        for i in range(n):
            disjoint.add(self.find(parent, i))

        return len(disjoint)
        
    def are_similar(self, s1, s2):
        diff = 0
        for a, b in zip(s1, s2):
            if a != b:
                diff += 1
                if diff > 2:
                    return False
        return True
    
    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y