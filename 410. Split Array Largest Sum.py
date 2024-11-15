class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)

        if k == 1:
            return right
        if k==len(nums):
            return left
        
        while left <= right:
            mid = left + (right-left)//2
            num_sub = self.split(nums, mid)
            if num_sub > k:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def split(self, nums, target):
        cnt = 1
        cur_sum = 0
        for n in nums:
            if cur_sum + n > target:
                cnt += 1
                cur_sum = n
            else:
                cur_sum += n
        return cnt