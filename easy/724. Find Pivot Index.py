class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum = [0] * n
        rightSum = [0] * n

        for idx in range(n):
            if idx != 0:
                leftSum[idx] = leftSum[idx-1] + nums[idx-1]
                rightSum[n-idx-1] = rightSum[n-idx] + nums[n-idx]
        
        for idx in range(n):
            if leftSum[idx] == rightSum[idx]:
                return idx
        return -1