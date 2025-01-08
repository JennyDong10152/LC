class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        increment = decrement = answer = 0

        for idx in range(len(nums)):
            difference = target[idx] - nums[idx]

            if difference > 0:
                if increment < difference:
                    answer += difference - increment
                increment = difference
                decrement = 0
            elif difference < 0:
                if decrement < -difference:
                    answer += -difference - decrement
                decrement = -difference
                increment = 0
            else:
                increment = 0
                decrement = 0
        return answer