class Solution:
    def findMedianSortedArrays(self, A: List[int], B: List[int]) -> float:
        len_a, len_b = len(A), len(B)
        total_len = len_a + len_b
        self.A = A
        self.B = B
        print(1//2)

        if total_len % 2: #odd
            return self.solve(total_len // 2, 0, len_a-1, 0, len_b-1)
        else:
            return (
                self.solve(total_len // 2 - 1, 0, len_a-1, 0, len_b-1)
                + self.solve(total_len // 2, 0, len_a-1, 0, len_b-1)
            ) / 2
    
    def solve(self, k, left_a, right_a, left_b, right_b):

            if left_a > right_a:
                return self.B[k - left_a]
            if left_b > right_b:
                return self.A[k - left_b]

            mid_a = left_a + (right_a - left_a) // 2
            mid_b = left_b + (right_b - left_b) // 2
            midV_a = self.A[mid_a]
            midV_b = self.B[mid_b]

            if mid_a + mid_b < k: #move right
                if midV_a > midV_b:
                    return self.solve(k, left_a, right_a, mid_b + 1, right_b)
                else:
                    return self.solve(k, mid_a + 1, right_a, left_b, right_b)

            else:
                if midV_a > midV_b:
                    return self.solve(k, left_a, mid_a - 1, left_b, right_b)
                else:
                    return self.solve(k, left_a, right_a, left_b, mid_b - 1)