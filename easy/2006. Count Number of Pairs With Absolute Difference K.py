class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        frequency = defaultdict(int)
        count = 0
        for num in nums:
            frequency[num] += 1
            count += frequency[num+k]
            count += frequency[num-k]
        return count