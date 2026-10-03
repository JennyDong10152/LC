class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        parent = [i for i in range(n)]

        for u in range(n):
            root_u = self.find(parent, u)
            for v in graph[u]:
                root_v = self.find(parent, v)
                if root_u == root_v:
                    return False
                parent[root_v] = self.find(parent, graph[u][0])
        return True
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]