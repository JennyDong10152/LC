class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        interval = []
        n = len(intervals)
        ans = [-1] * n

        for idx, [start, end] in enumerate(intervals):
            interval.append([start, end, idx])
        
        interval.sort()
        for start, end, idx_o in interval:
            idx = self.find(interval, end)
            if 0<=idx<n:
                ans[idx_o] = interval[idx][2]
        return ans
    
    def find(self, interval, target):
        left = 0
        right = len(interval) - 1

        while left <= right:
            mid = left + (right - left) // 2
            midV = interval[mid][0]
            if midV >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left