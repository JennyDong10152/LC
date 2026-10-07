class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        maxLength = 0
        frequency = defaultdict(int)

        for right, fruit in enumerate(fruits):
            frequency[fruit] += 1
            while len(frequency) > 2:
                frequency[fruits[left]] -= 1
                if frequency[fruits[left]] == 0:
                    del frequency[fruits[left]]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength