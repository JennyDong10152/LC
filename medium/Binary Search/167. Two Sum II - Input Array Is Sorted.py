class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for idx1, num1 in enumerate(numbers):
            left = idx1 + 1
            right = len(numbers)-1

            while left <= right:
                mid = left + (right-left)//2
                midV = num1+numbers[mid]
                if midV == target:
                    return [idx1+1, mid+1]
                if midV > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return [-1, -1]