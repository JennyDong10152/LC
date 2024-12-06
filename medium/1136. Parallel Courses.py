class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        degree = [0] * (n+1)
        graph = defaultdict(list)

        for prev, course in relations:
            graph[prev].append(course)
            degree[course] += 1
        order= deque()
        semester = 0

        for i in range(1, n+1):
            if not degree[i]:
                order.append(i)
        
        while order:
            size = len(order)
            semester += 1
            for _ in range(size):
                curr = order.popleft()
                for course in graph[curr]:
                    degree[course] -= 1
                    if not degree[course]:
                        order.append(course)
        return semester if not any(degree) else -1