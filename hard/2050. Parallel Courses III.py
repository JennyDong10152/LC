class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)
        degree = [0] * (n+1)
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
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                waitTime[neighbor] = max(waitTime[neighbor], time[neighbor-1] + waitTime[curr])
                maxWaitTime = max(maxWaitTime, waitTime[neighbor])
                if not degree[neighbor]:
                    q.append(neighbor)
        return maxWaitTime