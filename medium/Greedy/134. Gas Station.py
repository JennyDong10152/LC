class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total = 0
        current = 0
        ans = 0

        for idx in range(len(gas)):
            if current < 0:
                current = 0
                ans = idx 
            total += gas[idx] - cost[idx]
            current += gas[idx] - cost[idx]
        return ans if total >= 0 else -1