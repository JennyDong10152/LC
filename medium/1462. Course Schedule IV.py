class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        ans = []
        for parent, child in prerequisites:
            graph[parent].append(child)
        
        for parent, child in queries:
            ans.append(self.check(parent, child, graph))
        return ans
    
    def check(self, parent, child, graph):
        visited = set()
        q = deque([parent])

        while q:
            course = q.popleft()
            visited.add(course)
            if course == child:
                return True
            for c in graph[course]:
                if c not in visited:
                    q.append(c)
        return False