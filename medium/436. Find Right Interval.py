class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        ans = [-1] * n
        interval = []
        for idx, [start, end] in enumerate(intervals):
            interval.append([start, end, idx])
        interval.sort()
        
        for [start, end, idx_o] in interval:
            idx_right = self.search(interval, end)
            if 0 <= idx_right < n:
                ans[idx_o] = interval[idx_right][2]
        return ans
    
    def search(self, interval, target):
        left = 0
        right = len(interval)

        while left < right:
            mid = left + (right-left)//2
            midV = interval[mid][0]
            if midV >= target:
                right = mid
            else:
                left = mid + 1
        return left