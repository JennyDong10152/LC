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
            num_sub = self.search(nums, mid)
            if num_sub > k:
                left = mid + 1
            else:
                right = mid - 1
        return left
    
    def search(self, nums, mid):
        cnt = 1
        temp_sum = 0
        for n in nums:
            if temp_sum + n > mid:
                temp_sum = n
                cnt += 1
            else:
                temp_sum += n
        return cnt