import math
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)

        while left <= right:
            mid = left + (right-left)//2
            temp_sum = sum(math.ceil(i/mid) for i in nums)
            if temp_sum > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return left
        