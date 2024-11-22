class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_a = len(nums1)
        len_b = len(nums2)
        total = len_a + len_b
        self.A = nums1
        self.B = nums2
        if total % 2:
            return self.search(total//2, 0, len_a-1, 0, len_b-1)
        else:
            return (self.search(total//2-1, 0, len_a-1, 0, len_b-1) + self.search(total//2, 0, len_a-1, 0, len_b-1))/2
    
    def search(self, k, left_a, right_a, left_b, right_b):
        if left_a > right_a:
            return self.B[k-left_a]
        if left_b > right_b:
            return self.A[k-left_b]
        
        mid_a = left_a + (right_a-left_a) // 2
        mid_b = left_b + (right_b-left_b) // 2
        midV_a = self.A[mid_a]
        midV_b = self.B[mid_b]

        if mid_a + mid_b >= k:
            if midV_a > midV_b:
                return self.search(k, left_a, mid_a-1, left_b, right_b)
            else:
                return self.search(k, left_a, right_a, left_b, mid_b-1)
        else:
            if midV_a > midV_b:
                return self.search(k, left_a, right_a, mid_b+1, right_b)
            else:
                return self.search(k, mid_a+1, right_a, left_b, right_b)