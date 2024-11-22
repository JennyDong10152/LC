class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            left = i + 1
            right = len(numbers)-1
            while left <= right:
                mid = left + (right-left)//2
                midV = numbers[mid]
                if midV + n == target:
                    return [i+1, mid+1]
                elif midV + n > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return [-1, -1]