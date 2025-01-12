class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = sum(data)
        minimum = current = data[:window].count(0)
        for idx in range(window, len(data)):
            current -= not data[idx-window]
            current += not data[idx]
            minimum = min(minimum, current)
        return minimum