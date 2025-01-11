class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        frequency = defaultdict(int)

        for start, finish in zip(rounds, rounds[1:]):
            idx = start
            while True:
                frequency[idx] += 1
                if idx == finish:
                    break
                idx = (idx % n) + 1
        frequency[rounds[-1]] += 1

        max_frequency = max(frequency.values())
        result = [sector for sector, freq in frequency.items() if freq == max_frequency]

        return sorted(result)