class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(list)
        degree = [0] * n
        for more, less in richer:
            graph[more].append(less)
            degree[less] += 1
        
        q = deque()
        for i in range(n):
            if not degree[i]:
                q.append(i)
        ans = [i for i in range(n)]

        while q:
            curr = q.popleft()
            for poorer in graph[curr]:
                degree[poorer] -= 1
                if quiet[ans[poorer]] > quiet[ans[curr]]:
                    ans[poorer] = ans[curr]
                if not degree[poorer]:
                    q.append(poorer)
        return ans
