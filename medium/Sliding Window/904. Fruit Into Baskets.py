class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        maxLength = 0
        frequency = defaultdict(int)

        for right, fruit in enumerate(fruits):
            frequency[fruit] += 1
            if len(frequency) > 2:
                frequency[fruits[left]] -= 1
                if not frequency[fruits[left]]:
                    del frequency[fruits[left]]
                left += 1
<<<<<<< Updated upstream
            maxPicked = max(maxPicked, right - left + 1)
        return maxPicked
=======
            maxLength = max(maxLength, right - left + 1)
        return maxLength
>>>>>>> Stashed changes
