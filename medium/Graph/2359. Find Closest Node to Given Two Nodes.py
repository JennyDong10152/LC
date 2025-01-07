class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        neighbor1 = defaultdict(int)
        neighbor2 = defaultdict(int)
        self.reach(edges, neighbor1, node1)
        self.reach(edges, neighbor2, node2)

        distance = float("inf")
        answer = -1
        for node in neighbor1.keys() & neighbor2.keys():
            current_distance = max(neighbor1[node], neighbor2[node])
            if current_distance < distance:
                distance = current_distance
                answer = node
            if current_distance == distance:
                answer = min(answer, node)
        return answer

    def reach(self, edges, neighbor, source):
        current = source
        steps = 0
        while current != -1 and current not in neighbor:
            neighbor[current] = steps
            steps += 1
            current = edges[current]