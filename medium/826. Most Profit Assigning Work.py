class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = []
        for diff, pro in zip(difficulty, profit):
            jobs.append([diff, pro])
        jobs.sort()
        cur_max = 0
        for i, [_, pro] in enumerate(jobs):
            cur_max = max(cur_max, pro)
            jobs[i][1] = cur_max
        
        max_profit = 0
        for work in worker:
            cur_profit = self.search(jobs, work)
            max_profit += cur_profit
        return max_profit
    
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
        return jobs[left-1][1] if left > 0 else 0