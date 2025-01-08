class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        degree = defaultdict(int)

        for recipe, ingredient in zip(recipes, ingredients):
            for food in ingredient:
                graph[food].append(recipe)
                degree[recipe] += 1
        
        queue = deque()
        output = []
        for supply in supplies:
            queue.append(supply)
        
        while queue:
            food = queue.popleft()
            for recipe in graph[food]:
                degree[recipe] -= 1
                if not degree[recipe]:
                    output.append(recipe)
                    queue.append(recipe)
        return output