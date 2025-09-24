class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = []
        maxTotal = 0
        for diff, pro in zip(difficulty, profit):
            jobs.append([diff, pro])
        jobs.sort()

        maxProfit = 0
        for idx in range(len(jobs)):
            maxProfit = max(maxProfit, jobs[idx][1])
            jobs[idx][1] = maxProfit
        
        for w in worker:
            maxTotal += self.search(jobs, w)
        return maxTotal
    
    def search(self, jobs, target):
        left = 0
        right = len(jobs) - 1

        while left <= right:
            mid = left + (right - left)//2
            midV = jobs[mid][0]
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return jobs[right][1] if 0 <= right else 0