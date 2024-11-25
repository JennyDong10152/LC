class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
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
        return len(order) == numCourses