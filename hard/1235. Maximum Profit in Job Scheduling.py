class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = []
        n = len(startTime)
        for i in range(n):
            jobs.append([endTime[i], startTime[i], profit[i]])
        jobs.sort()

        dp = [0] * (n+1)
        for i, [_, cur_start, cur_profit] in enumerate(jobs):
            idx = self.search(jobs, cur_start, i)
            dp[i+1] = max(dp[i], cur_profit + dp[idx+1])
        return dp[n]
    
    
    def search(self, jobs, target, i):
        left = 0
        right = i - 1

        while left <= right:
            mid = left + (right-left)//2
            midV = jobs[mid][0]
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return right
