class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        if k == len(nums):
            return left
        if k == 1:
            return right
        
        while left <= right:
            mid = left + (right-left)//2
            num_sub = self.count(nums, mid)
            if num_sub > k:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def count(self, nums, target):
        temp_sum = 0
        cnt = 1

        for n in nums:
            if n + temp_sum > target:
                cnt += 1
                temp_sum = n
            else:
                temp_sum += n
        return cnt