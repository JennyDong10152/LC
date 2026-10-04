class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        heap = []
        intervals.sort()

        for start, end in intervals:
            if heap and heap[0] < start:
                heappop(heap)
            heappush(heap, end)
        return len(heap)