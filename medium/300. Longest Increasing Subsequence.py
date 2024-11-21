class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for n in nums:
            idx = self.search(ans, n)
            if idx < len(ans):
                ans[idx] = n
            else:
                ans.append(n)
        return len(ans)
    
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