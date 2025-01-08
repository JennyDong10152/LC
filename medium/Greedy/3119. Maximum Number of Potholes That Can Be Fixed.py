class Solution:
    def maxPotholes(self, road: str, budget: int) -> int:
        numConsecutive = []
        consecutive = 0
        answer = 0

        for path in road:
            if path == "x":
                consecutive += 1
            else:
                if consecutive != 0:
                    numConsecutive.append(consecutive)
                consecutive = 0
        if consecutive != 0:
                numConsecutive.append(consecutive)
        
        numConsecutive.sort(reverse=True)
        idx = 0

        while budget > 0 and idx < len(numConsecutive):
            if budget >= numConsecutive[idx]+1:
                answer += numConsecutive[idx]
            else:
                answer += budget - 1
            budget -= (numConsecutive[idx]+1)
            idx += 1
        return answer