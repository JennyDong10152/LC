class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = min(len(nums1), len(nums2))

        while left <= right:
            mid = left + (right - left) // 2
            found = self.find(nums1, nums2, mid)
            if found:
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    def find(self, nums1, nums2, length):
        nums1_set = set()
        for idx in range(length, len(nums1)+1):
            nums1_set.add(tuple(nums1[idx-length:idx]))
        
        for idx in range(length, len(nums2)+1):
            if tuple(nums2[idx-length:idx]) in nums1_set:
                return True
        return False