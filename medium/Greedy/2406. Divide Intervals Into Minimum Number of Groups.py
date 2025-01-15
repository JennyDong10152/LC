class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = []
        for start, end in intervals:
            if heap and heap[0] < start:
                heappop(heap)
            heappush(heap, end)
        return len(heap)