class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        missing = nums[-1]-nums[0] + 1 - n
        if missing < k:
            return nums[-1] + (k-missing)

        left = 0
        right = n-1
        curr = 0
        while left <= right:
            mid = left + (right-left)//2
            missing = nums[mid] - nums[curr] + 1 - (mid-curr+1)
            if missing >= k:
                right = mid - 1
            else:
                left = mid + 1
                k -= missing
                curr = mid
        return nums[curr] + k