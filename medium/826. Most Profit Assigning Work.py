class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [] #difficulty, profit
        for dif, pro in zip(difficulty, profit):
            jobs.append([dif, pro])
        jobs.sort()
        ans = 0
        max_profit = [0] * len(jobs)
        curr_max = 0
        for i in range(len(jobs)):
            curr_max = max(curr_max, jobs[i][1])
            max_profit[i] = curr_max
        
        for w in worker:
            left = 0
            right = len(jobs)-1
            while left <= right:
                mid = left + (right - left)//2
                if jobs[mid][0] > w:
                    right = mid - 1
                else:
                    left = mid + 1
            if left > 0:
                ans += max_profit[left-1]
        return ans