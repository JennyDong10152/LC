class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        left = 1
        right = num//2

        while left <= right:
            mid = left + (right-left)//2
            midV = mid * mid
            if midV == num:
                return True
            elif midV > num:
                right = mid-1
            else:
                left = left+1
        return False