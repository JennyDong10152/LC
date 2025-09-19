class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for idx, num in enumerate(numbers):
            left = idx + 1
            right = len(numbers) - 1

            while left <= right:
                mid = left + (right - left) // 2
                midV = numbers[mid] + num

                if midV == target:
                    return [idx+1, mid+1]
                elif midV > target:
                    right = mid - 1
                else:
                    left = mid + 1
        return [-1, -1]
