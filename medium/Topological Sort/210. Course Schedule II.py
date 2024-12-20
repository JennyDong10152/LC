class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * numCourses

        for course, prev in prerequisites:
            graph[prev].append(course)
            degree[course] += 1
        
        queue = deque()
        order = []
        for i in range(numCourses):
            if not degree[i]:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            order.append(curr)
            for course in graph[curr]:
                degree[course] -= 1
                if not degree[course]:
                    queue.append(course)
        return order if not any(degree) else []