class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        self.graph = defaultdict(list)
        for node in range(1, len(parent)):
            self.graph[parent[node]].append(node)
        self.answer = 0
        self.search(s, 0)
        return self.answer
    
    def search(self, s, node):
        root_char = s[node]
        longest = secondLongest = 0

        for child in self.graph[node]:
            childPath = self.search(s, child)
            if s[child] != root_char:
                if childPath >= longest:
                    secondLongest = longest
                    longest = childPath
                elif childPath >= secondLongest:
                    secondLongest = childPath
        self.answer = max(self.answer, 1 + longest + secondLongest)
        return 1 + longest
