class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        interval = []
        for idx, [i, j] in enumerate(intervals):
            interval.append([i,j,idx])
        interval.sort()

        starts = [i for i,_,_ in interval]
        ans = [-1] * len(starts)

        for i, j, idx_o in interval:
            left = 0
            right = len(interval)
            while left < right:
                mid = left + (right-left)//2
                midV = starts[mid]

                if midV >= j:
                    right = mid
                else:
                    left = mid+1
            if left < len(starts):
                ans[idx_o] = interval[left][2]
        return ans