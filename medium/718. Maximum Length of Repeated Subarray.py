class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = min(len(nums1), len(nums2))

        while left <= right:
            mid = left + (right-left)//2
            if self.hasCommon(nums1, nums2, mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
    
    def hasCommon(self, nums1, nums2, length):
        sub_nums1 = set()
        for i in range(len(nums1)-length+1):
            sub_nums1.add(tuple(nums1[i:i+length]))
        for i in range(len(nums2)-length+1):
            if tuple(nums2[i:i+length]) in sub_nums1:
                return True
        return False