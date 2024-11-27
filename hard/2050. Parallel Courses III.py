class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        degree = [0] * (n+1)
        graph = defaultdict(list)
        waitTime = [0] * (n+1)
        maxWaitTime = 0

        for prev, course in relations:
            graph[prev].append(course)
            degree[course] += 1
        
        q = deque()
        for i in range(1, n+1):
            if not degree[i]:
                q.append(i)
                waitTime[i] = time[i-1]
                maxWaitTime = max(maxWaitTime, waitTime[i])
        
        while q:
            curr = q.popleft()
            for course in graph[curr]:
                degree[course] -= 1
                waitTime[course] = max(waitTime[course], waitTime[curr]+time[course-1])
                maxWaitTime = max(maxWaitTime, waitTime[course])
                if not degree[course]:
                    q.append(course)
        return maxWaitTime