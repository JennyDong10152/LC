class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        frequency = defaultdict(int)
        maxLength = 0

        for right, fruit in enumerate(fruits):
            frequency[fruit] += 1
            while len(frequency) > 2:
                frequency[fruits[left]] -= 1
                if not frequency[fruits[left]]:
                    del frequency[fruits[left]]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength