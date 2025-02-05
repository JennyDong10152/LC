class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        n = len(target)
        count = target[0]
        for idx in range(n):
            if target[idx] > target[idx-1]:
                count += target[idx] - target[idx-1]
        return count