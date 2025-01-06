class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        self.tree = defaultdict(list)
        self.restricted = set(restricted)
        self.count = 0
        for node1, node2 in edges:
            self.tree[node1].append(node2)
            self.tree[node2].append(node1)
        self.search(0, -1)
        return self.count
    
    def search(self, node, parent):
        self.count += 1
        for child in self.tree[node]:
            if child == parent:
                continue
            if not child in self.restricted:
                self.search(child, node)