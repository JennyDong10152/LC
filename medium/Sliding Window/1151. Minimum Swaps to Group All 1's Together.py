class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = sum(data)
<<<<<<< Updated upstream
        swap = minSwap = data[:window].count(0)

        for right in range(window, len(data)):
            swap -= not data[right - window]
            swap += not data[right]
=======
        minSwap = swap = data[:window].count(0)

        for idx in range(window, len(data)):
            swap += not data[idx]
            swap -= not data[idx-window]
>>>>>>> Stashed changes
            minSwap = min(minSwap, swap)
        return minSwap