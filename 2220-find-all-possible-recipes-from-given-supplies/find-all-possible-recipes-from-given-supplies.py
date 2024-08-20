class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        suppliesSet = set(supplies)
        dependents = defaultdict(list)
        degree = defaultdict(int)
        
        for recipe, recipeIngredients in zip(recipes, ingredients):
            for ingredient in recipeIngredients:
                if ingredient not in suppliesSet:
                    degree[recipe] += 1
                    dependents[ingredient].append(recipe)
        
        queue = deque([recipe for recipe in recipes if not degree[recipe]])
        result = []
		
        while queue:
            front = queue.popleft()
            result.append(front)
            
            for dependent in dependents[front]:
                degree[dependent] -= 1
                if degree[dependent] == 0:
                    queue.append(dependent)
        
        return result