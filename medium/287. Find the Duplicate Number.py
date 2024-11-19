class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1
        dup = 0

        while left <= right:
            mid = left + (right-left)//2

            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                dup = mid
                right = mid - 1
        return dup