class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)

        for parent, child in prerequisites:
            graph[parent].append(child)
        ans = []
        for parent, child in queries:
            ans.append(self.check(parent, child, graph))
        return ans

    def check(self, parent, child, graph):
        q = deque([parent])
        visited = set()

        while q:
            curr = q.popleft()
            visited.add(curr)
            if curr == child:
                return True
            for course in graph[curr]:
                if not course in visited:
                    q.append(course)
        return False
            