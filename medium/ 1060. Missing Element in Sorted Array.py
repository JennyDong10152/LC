class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        missing = nums[-1] - nums[0] + 1 - n
        if k > missing:
            return nums[-1] + k - missing
        
        curr = 0
        left = 0
        right = n-1

        while left <= right:
            mid = left + (right - left) // 2
            missing = nums[mid] - nums[curr] + 1 - (mid-curr+1)
            if k > missing:
                curr = mid
                k -= missing
                left = mid + 1
            else:
                right = mid - 1
        return nums[curr] + k