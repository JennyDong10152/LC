class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minAns = arrays[0][0]
        maxAns = arrays[0][-1]
        answer = 0

        for array in arrays[1:]:
            answer = max(answer, array[-1] - minAns, maxAns - array[0])
            minAns = min(minAns, array[0])
            maxAns = max(maxAns, array[-1])
        return answer