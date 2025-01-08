class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        sameTime = []

        for start, end in intervals:
            if not sameTime or sameTime[0] > start:
                heappush(sameTime, end)
            else:
                heapreplace(sameTime, end)
        return len(sameTime)
