class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        graph = defaultdict(list)
        degree = [0] * (len(nums) + 1)

        for seq in sequences:
            for prev, curr in zip(seq, seq[1:]):
                if not curr in graph[prev]:
                    graph[prev].append(curr)
                    degree[curr] += 1
        
        order = deque()
        sequence = []
        for i in range(1, len(nums)+1):
            if not degree[i]:
                order.append(i)
        while order:
            size = len(order)
            if size >= 2:
                return False
            curr = order.popleft()
            sequence.append(curr)
            for num in graph[curr]:
                degree[num] -= 1
                if not degree[num]:
                    order.append(num)
        return sequence == nums