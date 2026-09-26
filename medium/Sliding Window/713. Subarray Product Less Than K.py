class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        product = 1
        if k < 2:
            return 0
        left = 0
        count = 0

        for right, num in enumerate(nums):
            product *= num
            while product >= k:
                product //= nums[left]
                left += 1

            count += right - left + 1
        return count