class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        divi = abs(dividend)
        div = abs(divisor)

        ans = int(self.binary_search(divi, div))

        if (dividend < 0) ^ (divisor < 0):
            ans = -ans

        return ans

    def binary_search(self, dividend, divisor):
        left = 0
        right = dividend
        ans = 0

        while left <= right:
            mid = left + (right - left) // 2
            num = divisor * mid
            if num == dividend:
                ans = mid
                break
            if num > dividend:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return ans
