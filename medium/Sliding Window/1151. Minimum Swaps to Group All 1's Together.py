class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = sum(data)
        swap = minSwap = data[:window].count(0)

        for idx in range(window, len(data)):
            swap -= not data[idx-window]
            swap += not data[idx]
            minSwap = min(minSwap, swap)
        return minSwap