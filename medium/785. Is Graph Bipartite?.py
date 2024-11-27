class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        parent = [i for i in range(n)]

        for i in range(n):
            root_i = self.find(parent, i)
            for j in range(len(graph[i])):
                root_j = self.find(parent, graph[i][j])
                if root_i == root_j:
                    return False
                self.union(parent, graph[i][0], graph[i][j])
        return True
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_x] = root_y

    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]