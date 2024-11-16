class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = [] #profit, start, end
        n = len(startTime)
        for i in range(n):
            jobs.append([endTime[i], startTime[i], profit[i]])
        jobs.sort()
        
        dp = [0] * (n+1)
        for i, (cur_end, cur_start, cur_profit) in enumerate(jobs):
            idx = self.search(cur_start, jobs, i)
            dp[i+1] = max(dp[i], dp[idx+1] + cur_profit)
        return dp[n]
    
    def search(self, target, jobs, i):
        left = 0
        right = i-1

        while left <= right:
            mid = left + (right-left)//2
            midV = jobs[mid][0]
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return right
        