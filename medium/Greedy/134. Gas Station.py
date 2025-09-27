class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        current = 0
        total = 0
        answer = 0

        for idx in range(len(gas)):
            current += gas[idx] - cost[idx]
            total += gas[idx] - cost[idx]
            if current < 0:
                answer = idx + 1
                current = 0
        return answer if total >= 0 else -1