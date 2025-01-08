class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        degree = [0] * (n+1)
        waitTime = [0] * (n+1)
        maxWaitTime = -1

        for prev, course in relations:
            graph[prev].append(course)
            degree[course] += 1
        
        queue = deque()
        for course in range(1, n+1):
            if not degree[course]:
                waitTime[course] = time[course-1]
                queue.append(course)
                maxWaitTime = max(maxWaitTime, waitTime[course])
        
        while queue:
            course = queue.popleft()
            for nextCourse in graph[course]:
                degree[nextCourse] -= 1
                waitTime[nextCourse] = max(waitTime[nextCourse], waitTime[course] + time[nextCourse-1])
                maxWaitTime = max(maxWaitTime, waitTime[nextCourse])
                if not degree[nextCourse]:
                    queue.append(nextCourse)
        return maxWaitTime