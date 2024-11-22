class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        multiple_of_ab = self.leastCommonFactor(a,b)
        multiple_of_bc = self.leastCommonFactor(b,c)
        multiple_of_ac = self.leastCommonFactor(a,c)
        multiple_of_abc = self.leastCommonFactor(a,multiple_of_bc)

        left = 1
        right = 2 * 10 ** 9
        while left <= right:
            mid = left + (right-left)//2
            cnt = mid//a + mid//b + mid//c - mid//multiple_of_ab - mid//multiple_of_bc - mid//multiple_of_ac + mid//multiple_of_abc
            if cnt >= n:
                right = mid - 1
            else:
                left = mid + 1
        return left

    
    def leastCommonFactor(self, x, y):
        def greatestCommonDivisor(x, y):
            if not x:
                return y
            return greatestCommonDivisor(y%x, x)
        return x * y / greatestCommonDivisor(x, y)