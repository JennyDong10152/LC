class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        stk = [(0,-1)] #prefix. idx
        prefix = 0
        min_length = float("inf")

        for i in range(len(nums)):
            prefix += nums[i]
            while stk and stk[-1][0] >= prefix:
                stk.pop()
            stk.append((prefix, i))
            idx = self.search(stk, prefix-k) #closest prefix smaller than prefix-k
            if idx != -1:
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