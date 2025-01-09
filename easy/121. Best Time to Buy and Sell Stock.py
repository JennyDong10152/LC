class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        least = prices[0]
        profit = 0

        for price in prices:
            if price < least:
                least = price
            profit = max(profit, price - least)
        return profit