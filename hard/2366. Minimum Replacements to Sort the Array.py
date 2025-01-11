class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i+1]:
                continue
            numElements = math.ceil(nums[i]/nums[i+1])
            answer += numElements - 1
            nums[i] = nums[i] // numElements
        return answer