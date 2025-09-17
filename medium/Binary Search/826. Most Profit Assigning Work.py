class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = []
        for diff, pro in zip(difficulty, profit):
            jobs.append([diff, pro])
        jobs.sort()
        maxTotal = 0
        
        max_profit = 0
        for i in range(len(jobs)):
            max_profit = max(max_profit, jobs[i][1])
            jobs[i] = (jobs[i][0], max_profit) 

        for w in worker:
            maxTotal += self.search(jobs, w)
        return maxTotal
    
    def search(self, jobs, target):
        left = 0
        right = len(jobs)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = jobs[mid][0]
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return jobs[right][1] if right >= 0 else 0