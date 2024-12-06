class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = [0] * numCourses
        graph = defaultdict(list)

        for course, prev in prerequisites:
            graph[prev].append(course)
            degree[course] += 1
        order = deque()

        for course in range(numCourses):
            if not degree[course]:
                order.append(course)
        
        while order:
            curr = order.popleft()
            for course in graph[curr]:
                degree[course] -= 1
                if not degree[course]:
                    order.append(course)
        return not any(degree)