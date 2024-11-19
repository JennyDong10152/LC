class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_idx = 0
        left = 0
        right = len(citations)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = citations[mid]
            rank = len(citations)-mid

            if midV >= rank:
                h_idx = rank
                right = mid - 1
            else:
                left = mid + 1
        return h_idx