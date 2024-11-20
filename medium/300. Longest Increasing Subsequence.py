class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for n in nums:
            if not sub or sub[-1] < n:
                sub.append(n)
            else:
                idx = self.search(n, sub)
                sub[idx] = n
        return len(sub)
    
    def search(self, target, nums):
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