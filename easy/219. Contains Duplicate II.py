class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        order = dict()
        for idx, num in enumerate(nums):
            if num in order and idx - order[num] <= k:
                return True
            order[num] = idx
        return False