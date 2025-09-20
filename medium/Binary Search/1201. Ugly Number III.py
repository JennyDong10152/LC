class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        multiple_ab = self.leastCommonFactor(a, b)
        multiple_bc = self.leastCommonFactor(c, b)
        multiple_ac = self.leastCommonFactor(a, c)
        multiple_abc = self.leastCommonFactor(a, multiple_bc)

        left = 1
        right = 2 * 10 ** 9

        while left < right:
            mid = left + (right - left) // 2
            cnt = mid//a + mid//b + mid//c - mid//multiple_ab - mid//multiple_bc - mid//multiple_ac + mid//multiple_abc
            if cnt >= n:
                right = mid
            else:
                left = mid + 1
        return left
    
    def leastCommonFactor(self, x, y):
        def greatestCommonDivisor(x, y):
            if not x:
                return y
            return greatestCommonDivisor(y%x, x)
        return x * y / greatestCommonDivisor(x, y)