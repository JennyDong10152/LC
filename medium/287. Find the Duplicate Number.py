class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)

        while left < right:
            mid = left + (right-left)//2
            cnt = 0
            for i in nums:
                if i <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        return right