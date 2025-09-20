class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = min(len(nums1), len(nums2))

        while left <= right:
            mid = left + (right - left) // 2
            contains = self.count(nums1, nums2, mid)
            if contains:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    def count(self, nums1, nums2, idx):
        nums1_set = set()

        for i in range(idx, len(nums1) + 1):
            nums1_set.add(tuple(nums1[i-idx:i]))
        
        for i in range(idx, len(nums2)+1):
            if tuple(nums2[i-idx:i]) in nums1_set:
                return True
        return False