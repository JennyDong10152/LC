class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = [0] * numCourses

        for course, prev in prerequisites:
            graph[prev].append(course)
            degree[course] += 1
        
        q = deque()
        for i in range(numCourses):
            if not degree[i]:
                q.append(i)

        order = []
        while q:
            curr = q.popleft()
            order.append(curr)
            for course in graph[curr]:
                degree[course] -= 1
                if not degree[course]:
                    q.append(course)
        return order if len(order)==numCourses else []