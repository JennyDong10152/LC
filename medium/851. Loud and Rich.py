class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        degree = [0] * n

        for more, less in richer:
            graph[more].append(less)
            degree[less] += 1
        
        order = deque()
        ans = [i for i in range(n)]
        for i in range(n):
            if not degree[i]:
                order.append(i)

        while order:
            curr = order.popleft()
            for less in graph[curr]:
                if quiet[ans[curr]] < quiet[ans[less]]:
                    ans[less] = ans[curr]
                degree[less] -= 1
                if not degree[less]:
                    order.append(less)
        return ans