class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        degree = [0] * (n+1)
        graph = defaultdict(list)

        for prev, course in relations:
            graph[prev].append(course)
            degree[course] += 1
        q = deque()
        cnt = 0
        courses_taken = []
        for i in range(1, n+1):
            if not degree[i]:
                q.append(i)
        
        while q:
            size = len(q)
            cnt += 1
            for _ in range(size):
                curr = q.popleft()
                courses_taken.append(curr)
                for course in graph[curr]:
                    degree[course] -= 1
                    if not degree[course]:
                        q.append(course)
        return cnt if len(courses_taken) == n else -1
    