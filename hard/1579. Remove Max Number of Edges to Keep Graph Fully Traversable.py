class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        parent_alice = [i for i in range(n + 1)]
        parent_bob = [i for i in range(n + 1)]

        required_edges = 0

        for edge_type, u, v in edges:
            if edge_type == 3:
                alice = self.union(parent_alice, u, v)
                bob = self.union(parent_bob, u, v)
                if alice or bob:
                    required_edges += 1

        for edge_type, u, v in edges:
            if edge_type == 1:
                if self.union(parent_alice, u, v):
                    required_edges += 1

        for edge_type, u, v in edges:
            if edge_type == 2:
                if self.union(parent_bob, u, v):
                    required_edges += 1

        alice_connected = len(set(self.find(parent_alice, i) for i in range(1, n + 1)))
        bob_connected = len(set(self.find(parent_bob, i) for i in range(1, n + 1)))
        if alice_connected != 1 or bob_connected != 1:
            return -1

        return len(edges) - required_edges

    def find(self, parent, x):
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if root_x != root_y:
            parent[root_y] = root_x 
            return True
        return False