class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons = persons
        leading = -1
        self.vote_cnt = {}
        self.leadings = []

        for p in persons:
            if not p in self.vote_cnt:
                self.vote_cnt[p] = 0
            self.vote_cnt[p] += 1
            if leading == -1 or self.vote_cnt[p] >= self.vote_cnt[leading]:
                leading = p
            self.leadings.append(leading)
        
    def q(self, t: int) -> int:
        idx = self.search(t)
        return self.leadings[idx] if idx>=0 else None
    
    def search(self, target):
        left = 0
        right = len(self.times)-1

        while left <= right:
            mid = left + (right-left)//2
            midV = self.times[mid]
            if midV > target:
                right = mid - 1
            else:
                left = mid + 1
        return right