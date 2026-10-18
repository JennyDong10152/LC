class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        maxDis = 0
        curMin = arrays[0][0]
        curMax = arrays[0][-1]

        for array in arrays[1:]:
            maxDis = max(maxDis, curMax-array[0], array[-1]-curMin)
            curMax = max(curMax, array[-1])
            curMin = min(curMin, array[0])
        return maxDis