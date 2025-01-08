class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * numCourses

        for course, prev in prerequisites:
            graph[prev].append(course)
            degree[course] += 1
        
        queue = deque()
        order = []

        for course in range(numCourses):
            if not degree[course]:
                queue.append(course)
        
        while queue:
            course = queue.popleft()
            order.append(course)
            for nextCourse in graph[course]:
                degree[nextCourse] -= 1
                if not degree[nextCourse]:
                    queue.append(nextCourse)
        return order if not any(degree) else []