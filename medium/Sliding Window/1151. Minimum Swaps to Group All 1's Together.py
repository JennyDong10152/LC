class Solution:
    def minSwaps(self, data: List[int]) -> int:
        window = sum(data)
        swap = minSwap = data[:window].count(0)
        for right in range(window, len(data)):
            swap -= not data[right - window]
            swap += not data[right]
            minSwap = min(minSwap, swap)
        return minSwap