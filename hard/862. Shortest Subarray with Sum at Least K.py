class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        stk = [(0, -1)]
        min_length = len(nums)+1
        prefix = 0

        for i, n in enumerate(nums):
            prefix += n
            while stk and stk[-1][0] >= prefix:
                stk.pop()
            stk.append((prefix, i))
            #prefix - k >= target
            idx = self.search(stk, prefix - k)
            if 0 <= idx < len(stk):
                min_length = min(min_length, i-stk[idx][1])
        return min_length if min_length != len(nums)+1 else -1

    
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