from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        prereq = defaultdict(list)
        degree = [0] * numCourses

        for child, parent in prerequisites:
            prereq[parent].append(child)
            degree[child] += 1
        noMorePrereq = deque()
        for idx, n in enumerate(degree):
            if not n:
                noMorePrereq.append(idx)

        cnt = 0
        while noMorePrereq:
            parent = noMorePrereq.popleft()
            cnt += 1
            for child in prereq[parent]:
                degree[child] -= 1
                if not degree[child]:
                    noMorePrereq.append(child)
        return cnt == numCourses