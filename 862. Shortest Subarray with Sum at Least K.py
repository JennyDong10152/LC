class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
<<<<<<< Updated upstream
        n = len(nums)
        stk = [(0, -1)] #sum, idx

        prefix = 0
        min_length = float("inf")

=======
        prefix = 0
        min_length = float("inf")
        n = len(nums)
        stk = [(0,-1)]
        
>>>>>>> Stashed changes
        for i in range(n):
            prefix += nums[i]
            while stk and prefix <= stk[-1][0]:
                stk.pop()

            stk.append((prefix, i))
            idx = self.search(stk, prefix - k) #prefix-prev_prefix >= k

            if idx != -1:
                min_length = min(min_length, i - stk[idx][1])

        return min_length if min_length != float("inf") else -1
        

    def search(self, nums, target):
        left = 0
<<<<<<< Updated upstream
        right = len(nums) - 1
=======
        right = len(nums)-1
>>>>>>> Stashed changes

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid][0] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right