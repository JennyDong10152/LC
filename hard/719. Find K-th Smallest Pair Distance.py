class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        right = nums[-1]-nums[0]

        while left < right:
            mid = left + (right-left)//2
            if self.search(nums, mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left
    

    def search(self, nums, mid):
        cnt = 0
        left = 0
        for right in range(1, len(nums)):
            while nums[right]-nums[left] > mid:
                left += 1
            cnt += (right-left)
        return cnt