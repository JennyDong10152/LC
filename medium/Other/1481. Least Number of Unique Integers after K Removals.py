class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequency = defaultdict(int)
        for num in arr:
            frequency[num] += 1

        frequency = sorted(frequency.items(), key=lambda item: item[1])

        removed = 0
        for key, freq in frequency:
            if k >= freq:
                k -= freq
                removed += 1
            else:
                break

        unique = len(frequency)
        remaining = unique - removed
        return remaining