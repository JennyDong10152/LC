class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        parent = [i for i in range(n+1)]
        graph = defaultdict(list)
        
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(1, n+1):
            root_i = self.find(parent, i)
            for j in graph[i]:
                root_j = self.find(parent, j)
                if root_i == root_j:
                    return False
                self.union(parent, graph[i][0], j)
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
