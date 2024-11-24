class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_sum = -1
        for i, n in enumerate(nums):
            idx = self.search(n, k, nums, i)
            print(n, nums[idx])
            if idx > i:
                max_sum = max(max_sum, nums[idx]+n)
        return max_sum
    
    def search(self, n, target, nums, idx):
        left = idx + 1
        right = len(nums)-1

        while left <= right:
            mid = left + (right - left)//2
            midV = nums[mid]
            if midV + n >= target:
                right = mid - 1
            else:
                left = mid + 1
        return right