class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        prereq = defaultdict(list)
        degree = [0] * numCourses

        for child, parent in prerequisites:
            prereq[parent].append(child)
            degree[child] += 1
        
        noMorePrereq = deque()
        for i, n in enumerate(degree):
            if not n:
                noMorePrereq.append(i)
        
        while noMorePrereq:
            parent = noMorePrereq.popleft()
            order.append(parent)
            for child in prereq[parent]:
                degree[child] -= 1
                if not degree[child]:
                    noMorePrereq.append(child)
        return order if len(order) == numCourses else []