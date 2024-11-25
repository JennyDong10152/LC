class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        recipe = defaultdict(list) #ingredient : [food created with the ingredient]
        degree = defaultdict(int) #food : count of ingredients needed

        for i, ingredient in enumerate(ingredients):
            for ing in ingredient:
                recipe[ing].append(recipes[i])
                degree[recipes[i]] += 1

        q = deque()
        ans = []
        for supply in supplies:
            q.append(supply)
        
        while q:
            cur = q.popleft()
            for food in recipe[cur]:
                degree[food] -= 1
                if not degree[food]:
                    ans.append(food)
                    q.append(food)
        return ans