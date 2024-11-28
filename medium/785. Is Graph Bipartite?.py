class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        parent = [i for i in range(n)]
        
        for i in range(n):
            parent_root = self.find(parent, parent[i])
            for j in range(len(graph[i])):
                neighbor_root = self.find(parent, graph[i][j])
                if parent_root == neighbor_root:
                    return False
                self.union(parent, graph[i][0], graph[i][j])
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