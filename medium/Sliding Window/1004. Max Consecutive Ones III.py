class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        maxLength = 0
        count = 0

        for right, num in enumerate(nums):
            count += not num
            while count > k:
                count -= not nums[left]
                left += 1
            maxLength = max(maxLength, right - left + 1)
<<<<<<< Updated upstream
        return maxLength
=======
        return maxLength
                
>>>>>>> Stashed changes
