class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        left = 0
        right = len(citations) - 1
        h_idx = 0 

        while left <= right:
            mid = left + (right - left) // 2
            citation_count = citations[mid]
            paper = n - mid

            if citation_count >= paper:
                h_idx = paper
                right = mid - 1
            else:
                left = mid + 1
        return h_idx