class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        negativeCount = 0
        minValue = float("inf")

        for row in matrix:
            for value in row:
                total += abs(value)
                if value < 0:
                    negativeCount += 1
                minValue = min(minValue, abs(value))
        if negativeCount % 2:
            total -= 2 * minValue
        return total