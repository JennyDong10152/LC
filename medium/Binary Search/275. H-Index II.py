class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        left = 0
        right = n-1
        h_idx = 0

        while left <= right:
            mid = left + (right-left)//2
            midV = citations[mid]
            rank = n-mid
            if midV >= rank:
                h_idx = rank
                right = mid - 1
            else:
                left = mid + 1
        return h_idx