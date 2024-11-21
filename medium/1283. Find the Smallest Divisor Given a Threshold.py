import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left < right:
            mid = left + (right-left)//2
            if self.isValid(nums, mid, threshold):
                right = mid
            else:
                left = mid + 1
        return right
    
    def isValid(self, nums, div, threshold):
        sums = 0
        for n in nums:
            sums += int(math.ceil(n / div))
        return sums <= threshold