class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c)+1)):
            b = c - a * a
            if self.isSquare(b):
                return True
        return False
    
    def isSquare(self, target):
        left = 0
        right = target

        while left <= right:
            mid = left + (right-left)//2
            midV = mid * mid
            if midV == target:
                return True
            elif midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return False