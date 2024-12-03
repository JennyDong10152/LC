class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = left =0 
        right = len(nums)-1
        while left < right:
            if nums[right]+nums[left]>=target:
                right -= 1
            else:
                res += right-left
                left += 1
        return res