class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        graph = defaultdict(list)
        for start, end in enumerate(edges):
            graph[end].append(start)

        n = len(edges)
        minNode = 0
        maxScore = -1

        for node in range(n):
            score = sum(graph[node])
            if score > maxScore:
                maxScore = score
                minNode = node
        return minNode