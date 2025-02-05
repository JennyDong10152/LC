class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left = 0
        right = max(quantities)
        while left < right:
            mid = left + (right - left) // 2
            if self.canDistribute(mid, quantities, n):
                right = mid
            else:
                left = mid + 1
        return left
    
    def canDistribute(self, x, quantities, n):
        j = 0
        remaining = quantities[j]
        for idx in range(n):
            if remaining <= x:
                j += 1
                if j == len(quantities):
                    return True
                else:
                    remaining = quantities[j]
            else:
                remaining -= x
        return False