class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)
        graph = {i : [] for i in range(1, n+1)}
        degree = [0] * (n+1)

        for seq in sequences:
            for prev, curr in zip(seq, seq[1:]):
                if not curr in graph[prev]:
                    graph[prev].append(curr)
                    degree[curr] += 1
        q = deque()
        for i in range(1, n+1):
            if not degree[i]:
                q.append(i)

        order = []

        while q:
            size = len(q)
            if size >= 2:
                return False
            curr = q.popleft()
            order.append(curr)
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if not degree[neighbor]:
                    q.append(neighbor)
        return order == nums