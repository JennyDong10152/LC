class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        parent = [i for i in range(n)]

        for node in range(n):
            root_node = self.find(parent, node)
            for neighbor in graph[node]:
                root_neighbor = self.find(parent, neighbor)
                if root_node == root_neighbor:
                    return False
                parent[neighbor] = self.find(parent, graph[node][0])
        return True
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]