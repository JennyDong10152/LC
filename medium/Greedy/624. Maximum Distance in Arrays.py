class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        minAns = arrays[0][0]
        maxAns = arrays[0][-1]
        maxDis = 0

        for interval in arrays[1:]:
            maxDis = max(maxDis, maxAns - interval[0], interval[-1] - minAns)
            minAns = min(minAns, interval[0])
            maxAns = max(maxAns, interval[-1])
        return maxDis