class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        current = 0
        answer = 0

        for idx in range(len(gas)):
            total += gas[idx] - cost[idx]
            current += gas[idx] - cost[idx]
            if current < 0:
                current = 0
                answer = idx + 1
        return answer if total >= 0 else -1