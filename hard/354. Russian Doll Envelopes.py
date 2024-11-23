class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        ans = []
        heights = [envelope[1] for envelope in envelopes]

        for height in heights:
            idx = self.search(ans, height)
            if idx == len(ans):
                ans.append(height)
            else:
                ans[idx] = height
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