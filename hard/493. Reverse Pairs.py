class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sorted_nums = []
        cnt = 0
        
        for n in reversed(nums):
            target = n / 2
            idx = self.search(sorted_nums, target)
            cnt += idx
            idx_inserted = self.search(sorted_nums, n)
            sorted_nums.insert(idx_inserted, n)
        return cnt
    
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid]
            if midV >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left