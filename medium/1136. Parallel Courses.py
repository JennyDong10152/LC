class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        degree = [0] * (n+1)
        graph = defaultdict(list)

        for prev, course in relations:
            graph[prev].append(course)
            degree[course] += 1
        
        q = deque()
        for i in range(1, n+1):
            if not degree[i]:
                q.append(i)
        
        course_taken = 0
        cnt = 0

        while q:
            size = len(q)
            for _ in range(size):
                course = q.popleft()
                course_taken += 1
                for next_course in graph[course]:
                    degree[next_course] -= 1
                    if not degree[next_course]:
                        q.append(next_course)
            cnt += 1
        return cnt if course_taken == n else -1