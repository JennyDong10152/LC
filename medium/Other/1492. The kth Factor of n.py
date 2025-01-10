class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for factor in range(1, n+1):
            if not n % factor:
                factors.append(factor)
        return factors[k-1] if k <= len(factors) else -1