class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        disjoint = n
        parent = [i for i in range(n)]
        for node1, node2 in edges:
            connect = self.union(parent, node1, node2)
            if connect:
                disjoint -= 1
        return disjoint
    
    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False
    
    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find(parent, parent[x])
        return parent[x]