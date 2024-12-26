class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for node1, node2 in paths:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        answer = [0] * n
        
        for garden in range(1, n+1):
            colors = set([1, 2, 3, 4])
            for neighbor in graph[garden]:
                if answer[neighbor-1] in colors:
                    colors.remove(answer[neighbor-1])
            answer[garden-1] = colors.pop()
        return answer