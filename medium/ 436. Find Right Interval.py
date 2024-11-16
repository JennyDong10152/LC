class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        if not intervals:
            return [-1]

        ans = [-1] * len(intervals)
        interval = []
        for idx, [i, j] in enumerate(intervals):
            interval.append([i, j, idx])
        
        interval.sort()
        for i, j, idx_o in interval:
            left = 0
            right = len(interval)

            while left < right:
                mid = left + (right-left)//2
                midV = interval[mid][0]
                if midV >= j:
                    right = mid
                else:
                    left = mid + 1
            if left < len(interval):
                ans[idx_o] = interval[left][2]
        return ans