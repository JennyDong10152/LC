class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right-left)//2
            days_needed = self.search(weights, mid)
            if days_needed > days:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def search(self, nums, target):
        cnt = 1
        curr = 0
        for n in nums:
            if n + curr > target:
                cnt += 1
                curr = n
            else:
                curr += n
        return cnt