class Solution:
    def minOperations(self, nums: List[int], x: int, y: int) -> int:
        x, y = max(x, y), min(x, y)

        left = 0
        right = max(nums) // min(x, y) + 1
        last_acceptable = -1

        while left <= right:
            mid = left + (right-left)//2

            acceptable = self.check_nums(mid, x, y, nums)
            if acceptable:
                right = mid - 1
                last_acceptable = mid
            else:
                left = mid + 1

        return last_acceptable

    def check_nums(self, num_steps, x, y, nums):
        baseline = y * num_steps
        x_bank = num_steps

        for n in nums: 
            residual = n - baseline
            if residual > 0:
                x_bank -= math.ceil(residual / (x - y))
            
                if x_bank < 0:
                    return False
        return True
