class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        min_length = float('inf')
        stk = [(0, -1)] #prefix, idx
        prefix = 0

        for i in range(len(nums)):
            prefix += nums[i]
            #cur_prefix - target >= k
            #cur_prefix - k >= target
            while stk and stk[-1][0] >= prefix:
                stk.pop()
            stk.append((prefix, i))
            target = prefix-k
            idx = self.search(stk, target)
            if idx >= 0:
                min_length = min(min_length, i-stk[idx][1])
        return min_length if min_length != float("inf") else -1
    
    def search(self, nums, target):
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = nums[mid][0]
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return right