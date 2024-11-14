class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = self.lcm(a, b)
        bc = self.lcm(b, c)
        ac = self.lcm(a, c)
        abc = self.lcm(a, bc)

        left = 1
        right = 2 * 10**9
        ans = 0

        while left <= right:
            mid = left + (right-left)//2
            cnt = mid//a + mid//b + mid//c - mid//ab - mid//bc - mid//ac + mid//abc
            if cnt >= n:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
    
    def lcm(self, a, b):
        def gcd(a, b):
            if not a:
                return b
            return gcd(b%a, a)
        return a * b // gcd(a, b)
