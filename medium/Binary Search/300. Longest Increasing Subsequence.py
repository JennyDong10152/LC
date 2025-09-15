class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        for num in nums:
            idx = self.search(ans, num)
            if idx < len(ans):
                ans[idx] = num
            else:
                ans.append(num)
        return len(ans)
    
    def search(self, array, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            midV = array[mid]

            if midV >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left