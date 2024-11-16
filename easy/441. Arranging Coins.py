class Solution:
    def arrangeCoins(self, n: int) -> int:
        if not n:
            return 0
        left = 1
        right = n
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            coins = mid * (mid + 1) // 2
            if coins > n:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
            
        return ans