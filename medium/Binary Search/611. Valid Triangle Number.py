class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        if n < 3:
            return 0

        nums.sort()
        for target in range(2, n):
            left = 0
            right = target - 1
            while left < right:
                if nums[left] + nums[right] > nums[target]:
                    count += (right - left)
                    right -= 1
                else:
                    left += 1
        return count