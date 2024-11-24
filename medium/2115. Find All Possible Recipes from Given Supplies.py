class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        degree = defaultdict(int)
        recipe = defaultdict(list)

        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                recipe[ingredients[i][j]].append(recipes[i])
                degree[recipes[i]] += 1
        ans = []
        q = deque()
        for supply in supplies:
            q.append(supply)
        
        while q:
            ingredient = q.popleft()
            for i in recipe[ingredient]:
                degree[i] -= 1
                if not degree[i]:
                    ans.append(i)
                    q.append(i)
        return ans