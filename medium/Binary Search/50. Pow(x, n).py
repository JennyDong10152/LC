class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = self.calc(x, abs(n))
        if n < 0:
            return 1/ans
        return ans
    
    def calc(self, x, n):
        if not x:
            return 0
        if not n:
            return 1
        if n == 1:
            return x
        
        half = self.calc(x, n//2)
        if n % 2:
            return half * half * x
        return half * half