class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        degree = defaultdict(int)

        for i, ingredient in enumerate(ingredients):
            for ing in ingredient:
                graph[ing].append(recipes[i])
                degree[recipes[i]] += 1
        
        q = deque()
        ans = []
        for supply in supplies:
            q.append(supply)
        
        while q:
            curr = q.popleft()
            for food in graph[curr]:
                degree[food] -= 1
                if not degree[food]:
                    ans.append(food)
                    q.append(food)
        return ans