class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        parent = [i for i in range(n)]

        for i in range(n):
            root_i = self.find(parent, i)
            for neighbor in graph[i]:
                root_j = self.find(parent, neighbor)
                if root_i == root_j:
                    return False
                parent[root_j] = self.find(parent, graph[i][0])
        return True
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]