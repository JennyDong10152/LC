class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        maxDis = 0
        minCur = arrays[0][0]
        maxCur = arrays[0][-1]

        for array in arrays[1:]:
            maxDis = max(maxDis, maxCur - array[0], array[-1] - minCur)
            minCur = min(minCur, array[0])
            maxCur = max(maxCur, array[-1])
        return maxDis