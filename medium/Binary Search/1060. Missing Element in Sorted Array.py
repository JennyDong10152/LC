class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)
        missing = nums[-1] - nums[0] - n + 1 #total nums should be missing

        if k > missing:
            return nums[-1] + k-missing
        left = 0
        right = n-1
        curr = 0

        while left <= right:
            mid = left + (right-left)//2
            missing = nums[mid]-nums[curr]+1 - (mid-curr+1) 
            if k > missing:
                k -= missing
                left = mid + 1
                curr = mid
            else:
                right = mid - 1
        return nums[curr] + k