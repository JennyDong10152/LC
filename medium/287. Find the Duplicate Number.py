class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)

        while left <= right:
            mid = left + (right-left)//2
            cnt = 0
            for n in nums:
                if n <= mid:
                    cnt += 1
            if cnt > mid:
                right = mid - 1
            else:
                left = mid + 1
        return left
    #reviewed