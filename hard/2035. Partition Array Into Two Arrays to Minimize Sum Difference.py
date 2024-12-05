class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        half = n//2

        first_half = nums[:half]
        second_half = nums[half:]

        first_sequences = self.getSubsequenceSumWithElements(first_half)
        second_sequences = self.getSubsequenceSumWithElements(second_half)

        solution = abs(sum(first_half) - sum(second_half))

        total = sum(nums)
        half_total = total//2

        for k in range(1,half):
            left_elements = first_sequences[k]
            right_elements = sorted(second_sequences[half-k])

            for summ in left_elements:
                target = half_total - summ
                nearest_index = self.search(right_elements,target)

                for i in [nearest_index-1,nearest_index]:
                    if 0 <= i < len(right_elements):
                        left_subsequence = summ + right_elements[i]

                        # total = right_subsequence + left_subsequence
                        right_subsequence = total - left_subsequence 
                        solution = min(solution,abs(left_subsequence-right_subsequence))
        return solution
    
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            midV = nums[mid]
            if midV >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def getSubsequenceSumWithElements(self,arr):
        solution = {}
        n = len(arr)

        for k in range(1, n+1): 
            sums = []
            all_combinations = combinations(arr, k)
            for comb in all_combinations:
                sums.append(sum(comb))

            solution[k] = sums
        return solution