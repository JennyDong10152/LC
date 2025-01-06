class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.graph = defaultdict(list)
        for node in range(1, len(parent)):
            self.graph[parent[node]].append(node)
        self.path = 0
        self.search(s, 0)
        return self.path

    def search(self, s, current):
        deepest = secondDeepest = 0
        root_char = s[current]
        for child in self.graph[current]:
            depth = self.search(s, child)
            if s[child] != root_char:
                if depth >= deepest:
                    secondDeepest = deepest
                    deepest = depth
                elif depth >= secondDeepest:
                    secondDeepest = depth
        self.path = max(self.path, deepest + secondDeepest + 1)
        return deepest + 1