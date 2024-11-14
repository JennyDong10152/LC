class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        if k == 1:
            return right
        if k == len(nums):
            return left

        while left <= right:
            mid = left + (right-left)//2
            num_sub = self.split(mid, nums)
            if num_sub <= k:
                right = mid - 1
            else:
                left = mid + 1
        return left
    
    def split(self, target, nums):
        group = 1
        cur_sum = 0
        for n in nums:
            if cur_sum + n > target:
                cur_sum = n
                group += 1
            else:
                cur_sum += n
        return group