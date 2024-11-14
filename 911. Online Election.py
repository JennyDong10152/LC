class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.leadings = []
        self.times = times
        self.vote_cnt = {}
        leading = -1
        for i in range(len(persons)):
            person = persons[i]
            time = times[i]
            self.vote_cnt[person] = self.vote_cnt.get(person, 0) + 1
            
            if leading == -1 or self.vote_cnt[person] >= self.vote_cnt[leading]:
                leading = person
            self.leadings.append(leading)

    def q(self, t: int) -> int:
        idx = self.search(t)
        return self.leadings[idx] if idx >= 0 else None

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
        