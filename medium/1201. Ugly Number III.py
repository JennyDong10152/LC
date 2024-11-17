class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        multiples_of_ab = self.leastCommonFactor(a, b)
        multiples_of_bc = self.leastCommonFactor(b, c)
        multiples_of_ac = self.leastCommonFactor(a, c)
        multiples_of_abc = self.leastCommonFactor(a, multiples_of_bc)

        left = 0
        right = 2 * 10 ** 9
        ans = -1

        while left <= right:
            mid = left + (right-left)//2
            cnt = mid//a + mid//b + mid//c - mid//multiples_of_ab - mid//multiples_of_bc - mid//multiples_of_ac + mid//multiples_of_abc
            if cnt >= n:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
    
    def leastCommonFactor(self, x, y):
        def greatestCommonDivisor(x, y):
            if not x:
                return y
            return greatestCommonDivisor(y % x, x)
        return x * y / greatestCommonDivisor(x, y)