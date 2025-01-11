class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        frequency = defaultdict(int)

        for start, finish in zip(rounds, rounds[1:]):
            idx = start
            while start != finish:
                if start > n:
                    start = 1
                else:
                    frequency[start] += 1
                    start += 1
        frequency[rounds[-1]] += 1

        max_frequency = max(frequency.values())
        result = [sector for sector, freq in frequency.items() if freq == max_frequency]

        return sorted(result)
