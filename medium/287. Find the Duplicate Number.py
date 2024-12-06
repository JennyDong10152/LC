class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right-left)//2
            cnt = self.count(nums, mid)
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return left

    def count(self, nums, target):
        cnt = 0
        for n in nums:
            if n <= target:
                cnt += 1
        return cnt