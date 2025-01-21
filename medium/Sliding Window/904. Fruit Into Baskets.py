class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxPicked = 0
        left = 0
        basket = defaultdict(int)

        for right, fruit in enumerate(fruits):
            basket[fruit] += 1
            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if not basket[fruits[left]]:
                    del basket[fruits[left]]
                left += 1
            maxPicked = max(maxPicked, right - left + 1)
        return maxPicked