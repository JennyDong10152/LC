class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        graph = defaultdict(list)

        for course, prev in prerequisites:
            graph[prev].append(course)
            degree[course] += 1
        
        queue = deque()
        for course in range(numCourses):
            if not degree[course]:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            for nextCourse in graph[course]:
                degree[nextCourse] -= 1
                if not degree[nextCourse]:
                    queue.append(nextCourse)
        return not any(degree)