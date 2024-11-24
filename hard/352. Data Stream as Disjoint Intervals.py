class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        new_interval = [value, value]
        idx = self.search(value)
        if idx > 0 and self.intervals[idx-1][1]+1 >= value:
            idx -= 1
            new_interval[0] = self.intervals[idx][0]
            new_interval[1] = max(self.intervals[idx][1], value)
            del self.intervals[idx]
        
        while idx < len(self.intervals) and new_interval[1]+1 >= self.intervals[idx][0]:
            new_interval[1] = max(new_interval[1], self.intervals[idx][1])
            del self.intervals[idx]
        self.intervals.insert(idx, new_interval)

    def search(self, value):
        left = 0
        right = len(self.intervals)-1
        
        while left <= right:
            mid = left + (right-left)//2
            midV = self.intervals[mid][0]
            if midV >= value:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def getIntervals(self) -> List[List[int]]:
        return self.intervals