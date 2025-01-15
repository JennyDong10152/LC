class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = sum(data)
        swap = minSwap = data[:window].count(0)

        for i in range(window, len(data)):
            swap -= not data[i - window]
            swap += not data[i]
            minSwap = min(minSwap, swap)
        return minSwap