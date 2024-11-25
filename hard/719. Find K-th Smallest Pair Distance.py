class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1]-nums[0]

        while left < right:
            mid = left + (right-left)//2
            if k > self.count(nums, mid):
                left = mid + 1
            else:
                right = mid
        return right
    
    def count(self, nums, target):
        cnt = 0
        left = 0
        for right in range(1, len(nums)):
            while nums[right]-nums[left] > target:
                left += 1
            cnt += (right-left)
        return cnt