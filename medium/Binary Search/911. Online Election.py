class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        vote_cnt = {}
        self.leadings = []
        leading = -1

        for p in persons:
            if not p in vote_cnt:
                vote_cnt[p] = 0
            vote_cnt[p] += 1
            if leading == -1 or vote_cnt[p] >= vote_cnt[leading]:
                leading = p
            self.leadings.append(leading)

    def q(self, t: int) -> int:
        idx = self.search(t)
        return self.leadings[idx] if idx >=0 else None
    
    def search(self, t):
        left = 0 
        right = len(self.times)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = self.times[mid]
            if midV > t:
                right = mid - 1
            else:
                left = mid + 1
        return right 